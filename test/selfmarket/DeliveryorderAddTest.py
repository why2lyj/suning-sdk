#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-8-23

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.DeliveryorderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.deliveryDetail=[{"orderCode":"123456789","orderItem":"1","deliveryQty":"10","deliveryItemNo":"1"}]
a.deliveryHead={"plannedArrivalTime":"09:00","deliveryNo":"13456789","carrierName":"张三","supplierCode":"10000197","deliveryDate":"2018-01-01","carrierTel":"18669612345","plannedArrivalDate":"2018-01-01"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)