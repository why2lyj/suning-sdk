#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-5-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderRelationQueryRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("7413b0470380905d2330af7e445f1beb", "d9dc9254c32e5ba793793c0d203827c6")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.startTime='2015-01-07 19:40:55'
a.endTime='2015-01-08 19:40:58'
a.appId='1'
a.pageNo='1'
a.pageSize='10'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)