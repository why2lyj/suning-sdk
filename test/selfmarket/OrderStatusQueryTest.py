#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-11-18

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderStatusQueryRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("1579d631e43245840c515ffffdaea0a6", "165bb7a9d57c4feca55c719893d592b0")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.orderSource='201'
a.startTime='2015-11-01 12:20:00'
a.endTime='2015-11-13 12:20:00'
a.queryType='2'
a.pageSize='50'
a.pageNo='1'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)