#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-12-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderDeliveryAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("9416c0de5c17023f78ea058f541f5895", "6b86c422951046e2408da57f303241b0")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.outOrderId='201512280100011'
a.orderSource='201'
a.scheduleType='1'
a.deliveryType='1'
a.scheduleDay='2015-12-29 12:20:00'
a.scheduleStart='2015-12-29 12:20:00'
a.scheduleEnd='2015-12-29 12:20:00'
a.receiverZipCode='44'
a.receiverProvince='44'
a.receiverCity='44'
a.receiverArea='44'
a.receiverTown='44'
a.receiverAddress='44'
a.receiverName='44'
a.receiverMobile='44'
a.receiverPhone='44'
a.carCode='44'
a.orderFlag='44'
a.custSelectNumber='44'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)