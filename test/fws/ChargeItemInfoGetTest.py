#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-6-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ChargeItemInfoGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("95d3ca767adff5aa75adb0363de6f22b", "c0948c41fe19a358e50552cebc064514")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.serverId='2308'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)