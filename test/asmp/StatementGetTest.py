#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-6-21

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.StatementGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("5c991b791c6e5c46f925c7c6171a22cc", "911bc7ef82abc19f065f256d7afef2d9")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.guid='u00000000001'
a.zcjsqdm='123456789'
a.zawbs='1'
a.zkpje='123456'
a.noteHeader='æ '
a.factoryBp='0000020156 '
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)