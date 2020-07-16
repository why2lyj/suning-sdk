#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.GetLogisticsCrossbuyTaskRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("7671c52d74ce85fde1d219c7ad9d2c81", "c87d119d63660e4d6372f07a42d2e4e5")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.logisticOrderId='11'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)