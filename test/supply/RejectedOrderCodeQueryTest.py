#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-3-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.RejectedOrderCodeQueryRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("917f0b9a93b31393cf4d4816a84c2434", "917f0b9a93b31393cf4d4816a84c2433")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.startTime='2015-06-18 00:00:00'
a.endTime='2015-07-18 00:00:00'
a.pageNo='1'
a.pageSize='10'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)