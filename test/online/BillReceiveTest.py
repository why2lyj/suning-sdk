#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-1-9

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.BillReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.billDetailReqItemList=[{"cmmdtyCode":"761109110","tradeType":"1：正向，-1：逆向","goodsAmount":"50.00","orderItemId":"00113150469201","billDate":"2019-09-15","clearAmount":"55.00","settlementDifference":"2.00","clearDate":"2019-09-15","supplierCode":"0000000000","platformUsageFee":"2.00","settlementCommission":"2.00","transportFee":"10.00","promotionDiscount":"2.00","snCmmdtyName":"海尔空调999","receiveTime":"2019-09-15","platformDiscountAmount":"5.00","snCmmdtyCode":"11051100963","platformUsageDiscount":"5.00","settlementPrice":"56.00","suningDiscountAmount":"5.00","comment":"贵重物品、轻拿轻放。","promotionFee":"1.00","orderId":"MM000009847614"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)