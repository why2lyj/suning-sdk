#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-7-6

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SuporderstatusAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.supOrderStatus=[{"omsOrderNo":"123456","omsItemNo":"1","statusOccurTime":"yyyy-MM-dd","purOrderItemNo":"1","planArrTime":"yyyy-MM-dd","stateName":"已审核","notPassReasons":"货源不足","state":"11","purchaseOrderNo":"1001417778","number":"12","latestArrTime":"2017-08-09 "}]
a.supplierCode='10001097'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)