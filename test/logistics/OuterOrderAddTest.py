#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-8-7

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OuterOrderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("7727e111b255b1e5fc6fededcca6edc2", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.oriSys='ZZD'
a.orderItems={
  "orderItems": {
    "orderItem": {
      "orderId": "1004232622100105",
      "businessType": "B008",
      "shipCondition": "01",
      "pickupDate": "2015-08-04",
      "pickupTime": "23:22:22",
      "expectDate": "2015-08-10",
      "expectTime": "23:00:00",
      "createNumLes": "admin",
      "createDateLes": "2014-02-23",
      "createTimeLes": "12:02:23",
      "orderCustomer": "0010000011",
      "crossItems": {
        "crossItem": {
          "crossName": "aa",
          "remarks": "éè¦ç©å,è¯·è½»æ¿è½»æ¾"
        }
      },
      "orderPartners": {
        "orderPartner": [
          {
            "customerType": "AG",
            "customerId": "0010000016",
            "name": "zhagnshan",
            "address1": "ä»é¹¤é¨",
            "city": "åäº¬å¸",
            "district": "çæ­¦åº",
            "mobilePhone": "13412345670"
          },
          {
            "customerType": "WE",
            "customerId": "0010000016",
            "name": "zhangyu",
            "address1": "æå¤©å®«",
            "city": "åäº¬å¸",
            "district": "ç§¦æ·®åº",
            "mobilePhone": "12310101010"
          }
        ]
      }
    }
  }
}
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)