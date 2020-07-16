#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on 2014-05-21
@author: momo
"""
from suning.util.StringUtils import StringUtils

try:
    import httplib
except ImportError:
    import http.client as httplib
import os
import sys
import hashlib
import base64
import json
import re
import suning
from datetime import datetime
from suning.api.config import Const


class Configer():
    """
    可以使用此类更改默认参数配置
    """
    pass


def sign(appSecret, appMethod, date, appKey, content):
    # 签名方法
    baseStr = base64.b64encode(content).decode('utf_8')
    tomd5 = '%s%s%s%s%s%s' % tuple([appSecret, appMethod, date, appKey, Const.VERSION, baseStr])
    hashlib1 = hashlib.md5(tomd5.encode('utf_8'))

    return hashlib1.hexdigest()

class ParamException(Exception):
     
    u''' 操作结果抽象 '''
     
    def __init__(self, code, value=None):
        self.code = code   #操作结果代号
        self.value = value #操作结果值
         
    def __str__(self):
        return "operation result, code: %s, value: %s" % (self.code, self.value)

      
class RequestException(Exception):
    """
    API请求异常类
    """
    pass


class SuningApiException(Exception):
    """
    API调用异常类，包含两个变量
    <br>error_code: 异常码
    <br>message: 返回报文
    """

    def __init__(self):
        self.error_code = None
        self.message = None

    def __str__(self, *args, **kwargs):
        sb = "error_code=" + self.error_code + os.linesep + \
             "message=" + self.message
        return sb


class AbstractApi(object):
    """
    所有api接口的基类
    @param domain: 请求的域名或者ip
    @param port: 请求的端口
    """

    def __init__(self):
        self.__httpmethod = "POST"
        self.__apicontent = None  # 缓存请求报文
        self.__domain = Const.DOMAIN
        self.__port =  Const.PORT
        self.__accesstoken = None
        self.__paramrule = None
        if Const.ACCESS_TOKEN is not None:
            self.__accesstoken = Const.ACCESS_TOKEN
        if suning.getDefaultAppInfo():
            self.__app_key = suning.getDefaultAppInfo().appkey
            self.__secret = suning.getDefaultAppInfo().appsecrect
        else:
            self.__app_key = Const.APPKEY
            self.__secret = Const.APPSECRET
        self.__pointParams = None

    def getRequestHeader(self,apiContent):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        signInfo = sign(self.__secret, self.getApiMethod(), date, self.__app_key, apiContent)
        requestHeader = {
            "AppMethod": self.getApiMethod(),
            "AppRequestTime": date,
            "Format": Const.API_FORMAT,
            "AppKey": self.__app_key,
            "signInfo": signInfo,
            "VersionNo": Const.VERSION,
            'Content-type': 'application/json;charset=UTF-8',
            "Cache-Control": "no-cache",
            "Connection": "Keep-Alive",
            "User-Agent": "suning-sdk-python",
            "Sdk-Version" : Const.SDK_VERSION
        }
        if self.__accesstoken is not None:
            requestHeader["access_token"] = self.__accesstoken

        if self.__pointParams is not None:
            for key in self.__pointParams.keys():
                if key not in requestHeader:
                    requestHeader[key] = self.__pointParams[key]
        return requestHeader
    
    def setAppInfo(self, appkey, appsecret):
        """
        在运行时更改appkey 和appsecret
        @param appinfo:  
            a.setAppInfo(suning.appinfo("appkey","appsecret"))
        """
        self.__app_key = appkey
        self.__secret = appsecret
    
    def setDomainInfo(self, domain, port):
        self.__domain = domain
        self.__port = port
        
    '''
     @param accesstoken: accesstoken 支持oauth认证
    '''    
    def setAccessToken(self, accesstoken):
        self.__accesstoken = accesstoken

    def setPointParams(self, pointParams):
        self.__pointParams = pointParams

    def setParamRule(self, paramrule):
        self.__paramrule = paramrule
            
    def getApiMethod(self):
        return ""

    def getApiBizName(self):
        return ""



    def checkParam(self, param):
        regex_cache = {}
        if self.__paramrule is None:
            return;
        if param is None:
            return
        newdict = param.copy()
        for key in param.keys():
            if key.startswith("_"):
                newdict.pop(key)
        for key in newdict.keys():
            value = newdict[key]
            
            if key not in self.__paramrule:
                continue
            
            valid_rules = self.__paramrule[key]
            #验证规则
            #检测空
            allow_empty = valid_rules.get('allow_empty')
            if not allow_empty:
                if not value or not value.strip():
                    error = ParamException(key + "_empty", value);
                    raise error
                elif not value:
                    #如果是空的并且忽略空检测,那么下面的就不需要检查了
                    continue;
            #检测长度
            if 'min-length' in valid_rules:
                min_length = valid_rules['min-length']
                if min_length > len(value):
                    raise ParamException(key + "_length", value)
                         
            if 'max-length' in valid_rules:
                max_length = valid_rules['max-length']
                if max_length < len(value):
                    raise ParamException(key + "_length", value)
                     
            #检测正则
            if 'regex' in valid_rules:
                #获取编译后的正则
                regex = valid_rules['regex']
                regexcmp = regex_cache.get(regex)
                if not regexcmp:
                    regexcmp = re.compile(regex)
                    regex_cache[regex] = regexcmp
                if not regexcmp.search(value):
                    raise ParamException(key + "_format", value)
                     
                
    """
    @param paramdict: 需要转换的dict 
    @param enNone: 是否不转换None指变量 ，默认为True 
    @param enPirvate: 是否转换私有变量(start with ‘_’ and '__')，默认false，剔除私有变量 
    """
    def convertparamdict(self,paramdict,enNone=True, enPirvate=False):
        self.checkParam(paramdict);
        newdict = paramdict.copy()
        if enPirvate is False:  # 如果不转换私有变量
            for key in paramdict.keys():
                if key.startswith("_"):
                    newdict.pop(key)
        newdict2 = newdict.copy()            
        if enNone is True:
            for key in newdict.keys():
                value = newdict[key]
                if value is None:
                    newdict2.pop(key)
        return newdict2
                
    def getApiContent(self):
        """ 整理请求参数 """
        paramdict = self.convertparamdict(self.__dict__, True)
        """获取请求报文"""
        if sys.version_info[0] >= 3: 
            # 如果是python3.0以上环境，使用python内置dict转string函数，并对字符串进行encode
            self.__apicontent = ''.join(
            ['{"sn_request": { "sn_body": {"', self.getApiBizName(),'":', str(paramdict),
                '}}}']).encode("utf-8")
        else:
            # 如果低于python3.0，使用StringUtil工具进行dict转string
            self.__apicontent = ''.join(
            ['{"sn_request": { "sn_body": {"', self.getApiBizName(),'":', StringUtils().dict2string(paramdict),
                '}}}'])
        return self.__apicontent


    def _check_request(self):
        pass

    def getResponse(self):
        """
        获取服务器返回结果
        @return: 返回结果，json格式
        """
        if self.__port == "443":
            connection = httplib.HTTPSConnection(self.__domain, self.__port,None,None,Const.TIMEOUT)
        else:
            connection = httplib.HTTPConnection(self.__domain, self.__port, Const.TIMEOUT)
        connection.connect()
        
        apiContent = self.getApiContent()
        header = self.getRequestHeader(apiContent)
        body = apiContent
        connection.request(self.__httpmethod, Const.API_URI, body=body, headers=header)
        response = connection.getresponse()

        if response.status is not 200:
            raise RequestException('invalid http status ' + str(response.status) + ',detail body:' + response.read())
        result = response.read()
        result = result.decode('utf_8')
        jsonobj = json.loads(result)
        #print(StringUtils().dict2string(jsonobj));
        if "sn_responseContent" in jsonobj:
            if "sn_error" in jsonobj["sn_responseContent"]:
                error = SuningApiException()
                error.error_code = jsonobj["sn_responseContent"]["sn_error"]["error_code"]
                error.message = result
                raise error
        return jsonobj
