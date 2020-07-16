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

a=api.DiscountApplyAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a226186c2b811ce7fbce83e8a98dc7fe", "435687b33f10f5114a1d2440fe0848c7")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyHead=  {
          "supplierCode": "10001372",
          "supplierBraComp": "SEBJ",
          "supplierOffice": "北京,天津",
          "snCode": "5400",
          "supplierApplicationCode": "FYBJ14061004",
          "productBrand": "0123,0124,0125",
          "expenseBudgetCode": "123456789",
          "areaCopCode": "1001",
          "actionLettersCode": "12345",
          "chargeBudgetCode": "12345",
          "startDate": "2014-05-19",
          "endDate": "2014-05-29",
          "actionLettersContent": "经营活动函内容",
          "contractContent": "合同协议相关内容",
          "paymentLittleMount": "10000.60",
          "settlementType": "1",
          "payType": "3",
          "invoiceContent": "2",
          "payDate": "2014-05-26",
          "htmlContent": "XHHGHHKJKKKKLGFHJRTIOOJBK...",
          "signNatureContent": "XHHGHHKJKKKKLGFHJRTIOOJBK..."
        }


a.applyDetail=[
          {
            "chargeItem": "商业折让项目",
            "itemCode": "UAX60556XXZ",
            "wareNumber": "50",
            "onePrice": "1000.85",
            "salesAmount": "4545.45",
            "agioRate": "3",
            "settlementAmount": "5000.30"
          },
          {
            "chargeItem": "商业折让项目",
            "itemCode": "UAX60556XXJ",
            "wareNumber": "50",
            "onePrice": "1000.85",
            "salesAmount": "4545.45",
            "agioRate": "3",
            "settlementAmount": "5000.30"
          }
        ]

        


try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)