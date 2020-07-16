#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-4-20

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.FactoryServiceQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("82fdfb8aa13d18b1b3fd703b02f5d45e", "f73e8c8b9a0ef3b29a408fb71274edbd")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.recordGuId='1'
a.itemGuId='1'
a.srvOrdId='1'
a.startTime='2015-11-28 00:00:00'
a.endTime='2015-11-29 00:00:00'
a.pageNo='1'
a.pageSize='2'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)