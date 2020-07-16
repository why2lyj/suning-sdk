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

a=api.ApprovalResultQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("aa48c8b081c7d304a9b3f96725988f77", "4caf4cc47d7c114cb09d957a7454ddd3")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.supplierCode='10000007'
a.type='1'
a.applyCode='16802374'
a.createStartDate='2014-01-05'
a.createEndDate='2014-01-05'
a.modelType='1'
a.pageNo='1'
a.pageSize='10'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)