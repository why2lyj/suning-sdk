#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月5日
配置项
@author: dd
'''
class Const():
    VERSION = "v1.2"
    
    SDK_VERSION = "suning-sdk-python-beta0.1"
    
    #超时时间
    TIMEOUT = 10
    
    # api访问路径
    API_URI = "/api/http/sopRequest"
    
    #api请求格式，此sdk目前只支持json
    API_FORMAT = "json"
    
    #api 访问域名或IP
    DOMAIN = "openpre.cnsuning.com"
    
    #api 访问端口
    PORT = 80
    
    # API appkey 
    #APPKEY="4be597ae2ab497a06a75e2f8bea6f089"
    APPKEY = "cf97250875cd07d64fea3428dd3bd109"
    
    # API appsecret 
    # APPSECRET="dd565941167025fbe7431912133fbecd"
    APPSECRET= "9fb5785f3f84f60589329228182b0c0e"
    
    #AccessToken 默认为空
    ACCESS_TOKEN = None
    