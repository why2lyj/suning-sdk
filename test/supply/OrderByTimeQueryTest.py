#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-3-25

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderByTimeQueryRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("917f0b9a93b31393cf4d4816a84c2434", "917f0b9a93b31393cf4d4816a84c2433")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.startTime='2016-03-21 16:00:00'
a.endTime='2016-03-21 19:00:00'
a.orderLineStatus='10'
a.pageNo='1'
a.pageSize='2'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)