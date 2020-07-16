#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-1-11

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderDetailGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("", "")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.orderSource='301'
a.cancelType='1'
a.outOrderId='DP20160109005'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)