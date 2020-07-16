#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-3

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.MsgtaskCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appCode='短信控制台查看'
a.appSecret='短信控制台查看'
a.content='苏宁欢迎您'
a.interestActivityId='2020021600011245'
a.interestType='1'
a.longUrl='suning.com'
a.paramJson='{变量名1:变量值1,变量名2:变量值2}'
a.shortUrl='suning.com'
a.sign='苏宁'
a.taskChannel='1'
a.template='suning01'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)