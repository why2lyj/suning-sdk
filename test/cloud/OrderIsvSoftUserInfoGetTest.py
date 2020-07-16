#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-6-5

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderIsvSoftUserInfoGetRequest()

a.setDomainInfo("10.24.66.241","80")
a.setAppInfo("8f34a15bb19cb241630ce3aecaae0f8f", "e2074fb1ba5929709dc0a7185444b2c5")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.custNum='6001911196'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)