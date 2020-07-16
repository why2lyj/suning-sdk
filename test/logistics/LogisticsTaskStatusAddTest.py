#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-8-22

@author: suning
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.LogisticsTaskStatusAddRequest()
a.logisticOrderId="SNCY0200000008999"
a.logisticExpressId="62000000000000000001"
a.logisticStation="南京配送中心"
a.state="1020"
a.finishedDate="2014-06-23"
a.finishedTime="12:00:00"
a.consignee="admin"
a.operator="张三"
a.shipmentCode="test"
a.weight="22.2"
a.weightUnit="kg"
a.note="test"
a.airwayBillNo="test"
a.flightDate="test"
a.flightNo="test"


f = a.getResponse()
print(f)
