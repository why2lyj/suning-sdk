#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-3-6

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ExpensescheckorderQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applicationCode='1207X0021706148149'
a.applyCode='54862823'
a.createBegindate='2018-01-01'
a.createEnddate='2017-10-31'
a.modelType='1'
a.pageNo='1'
a.pageSize='10'
a.status='1'
a.supplierCode='10000007'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)