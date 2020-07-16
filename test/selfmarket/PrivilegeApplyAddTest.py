#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-4-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PrivilegeApplyAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a226186c2b811ce7fbce83e8a98dc7fe", "435687b33f10f5114a1d2440fe0848c7")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyHead= {
          "supplierCode": "10001372",
          "supplierBraComp": "SEBJ",
          "supplierOffice": "北京,天津",
          "snCode": "5400",
          "productBrand": "0123,0124,0125",
          "expenseBudgetCode": "123456789",
          "areaCopCode": "1001",
          "supplierApplicationCode": "HDGZ20140125",
          "startDate": "2014-05-19",
          "endDate": "2014-05-29",
          "applyLevel": "FGS",
          "actionDescribe": "优惠单活动函申请",
          "settlementType": "2",
          "payType": "3",
          "invoiceContent": "3",
          "payDate": "2014-05-29",
          "htmlContent": "XHHGHHKJKKKKLGFHJRTIOOJBK...",
          "signNatureContent": "XHHGHHKJKKKKLGFHJRTIOOJBK..."
        }
a.areaDetail= [
          {
            "operateAreaCompany": "1001",
            "operateAreaShoper": "所有门店"
          },
          {
            "operateAreaCompany": "1002",
            "operateAreaShoper": "所有门店"
          },
          {
            "operateAreaCompany": "1003",
            "operateAreaShoper": "所有门店"
          }
        ]
a.areaDetail=[
          {
            "wareHouse": "0001",
            "channel": "10",
            "itemCode": "LA52BLKCHN",
            "chargeItem": "999999",
            "favoureAmount": "500.15",
            "comments": "不参与XX活动"
          },
          {
            "wareHouse": "0001",
            "channel": "10",
            "itemCode": "LA52BLKCHN",
            "chargeItem": "999999",
            "favoureAmount": "500.15",
            "comments": "不参与XX活动"
          },
          {
            "wareHouse": "0001",
            "channel": "10",
            "itemCode": "LA52BLKCHN",
            "chargeItem": "999999",
            "favoureAmount": "500.15",
            "comments": "不参与XX活动"
          }
        ]


try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)