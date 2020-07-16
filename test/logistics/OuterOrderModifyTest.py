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

a=api.OuterOrderModifyRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("7727e111b255b1e5fc6fededcca6edc2", "a3719da1dc3eccf2d087cf2f53dafb83")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.oriSys='ZZD'
a.orderItems={
    "orderItem": [
        {
            "cashonDeliveryType": "02",
            "cashonDeliveryValue": "23",
            "changeDateTime": "2015-08-07 09:01:01",
            "changeFlag": "N",
            "changeReason": "ddd",
            "crossItems": {
                "crossItem": [
                    {
                        "crossWeight": "23",
                        "deliNumber": "ss",
                        "deliUnit": "dd",
                        "itemNumber": "20",
                        "remarks": "dd",
                        "volume": "dd",
                        "volumeUnit": "dd",
                        "weightUnit": "dd"
                    }
                ]
            },
            "expectDate": "2015-08-10",
            "expectTime": "23:00:00",
            "logisticsOrderId": "115080000254802",
            "orderPartners": {
                "orderPartner": [
                    {
                        "address1": "hh",
                        "address2": "ff",
                        "city": "hh",
                        "customerId": "0010000011",
                        "customerType": "WE",
                        "district": "ff",
                        "email": "666",
                        "fixedlineTelephone": "522",
                        "itemNumber": "20",
                        "mobilePhone": "55",
                        "name": "zhangyu",
                        "province": "333",
                        "region": "hhh",
                        "town": "fff",
                        "transportationZone": "555",
                        "zipCode": "52222"
                    }
                ]
            },
            "pickupDate": "2015-08-04",
            "pickupTime": "23:22:22"
        }
    ]
}
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)