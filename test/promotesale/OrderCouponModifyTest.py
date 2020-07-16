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

a=api.OrderCouponModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a368715446b62bafc9fb54a325f53c30", "a835b8afb4c86e7c7fe7ef527b2c0c31")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityCode='16010816421010001261'
a.activityName='1111'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)