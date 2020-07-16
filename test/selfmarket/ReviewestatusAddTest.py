#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-10-10

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReviewestatusAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.reviewestatus=[{"actualDeliveryTime":"2017-8-9","model":"1","omsOrderNo":"123456","statusOccurTime":"2017-04-08 20:00:00","state":"1","warehouseLocation":"12","serviceName":"123456","atpPlanArrWeek":"12","purOrderItemNo":"1","trafficDelayDays":"1","moneyAmount":"1","commArrTime":"2017-08-09 ","atpPlanArrDate":"2017-8-9","planDeliveryTime":"2017-08-09 ","industyArrTime":"2017-8-9","orderSource":"1","planArrTime":"2017-8-9","notPassReasons":"12","signQuantity":"1000000.333","industyTradeTime":"2017-8-9","custReceiptDate":"2017-8-9","number":"12","purchaseOrderNo":"1","latestArrTime":"2017-08-09 ","omsItemNo":"123","arrivalWeek":"1","serviceCode":"123456","confirmSubTime":"2017-08-09 17:03:43","arrivalDelayDays":"1"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)