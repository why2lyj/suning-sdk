#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-3-9

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.UnsaleStockReportQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("0dcb65d09590d6eb1b5b0d475f695959", "5826187b5ba4dbd9f414fdc7ecec6e6f")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.supplierCode='10026379'

a.pageNo='1'
a.pageSize='1'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)