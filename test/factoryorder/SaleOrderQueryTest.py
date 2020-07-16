#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-4-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SaleOrderQueryRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("1fffda2cb49365e770a1b4b266c471de", "87175f3d8e6ae538851e398f58438fba")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.startTime='2016-03-29 23:06:10'
a.endTime='2016-04-01 23:06:10'
a.pageNo='1'
a.pageSize='10'
a.state='40'
a.supplierCode='10000029'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)