#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-6-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ProductBackStorageAddRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("d4d39a8040fa16d9aa499a4af9b2a660", "3fde6dadef8515ea3ecf96ae4398d5c2")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.warehouseCode='L004'
a.refundType='0'
a.appointDate='2015-06-26'
a.appointTime='16:00'
a.contacts='1111'
a.supplierPhone='18626368253'
a.commodityList=[
             {
              "commodityCode": "100020001",
              "supCommCode": "B-10019",
              "refundCount": "15"
             },
             {
              "commodityCode": "100020002",
              "supCommCode": "B-10018",
              "refundCount": "20"
             }
            ]


try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)