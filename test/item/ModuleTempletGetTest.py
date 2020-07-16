#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-5-11

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ModuleTempletGetRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("fa6f80198cb2f2fe2c27d57b3b2d23ad", "dd2b44d25c542e9a6b82acd60005f539")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.categoryCode='R6151001'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)