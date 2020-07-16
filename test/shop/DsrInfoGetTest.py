#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-5-4

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.DsrInfoGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("2b3908fa221c2a3739ef324a560536b5", "dbd2fc8c99288cdad831afb823ae0328")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)