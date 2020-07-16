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

a=api.BalanceApplyAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a226186c2b811ce7fbce83e8a98dc7fe", "435687b33f10f5114a1d2440fe0848c7")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyHead={
          "supplierCode": "10001372",
          "supplierBraComp": "SEBJ",
          "supplierOffice": "北京,天津",
          "snCode": "5400",
          "supplierApplicationCode": "FYBJ14061004",
          "productBrand": "0123,0124,0125",
          "expenseBudgetCode": "123456789",
          "areaCopCode": "1001",
          "startDate": "2014-05-19",
          "endDate": "2014-05-29",
          "discountLittleMount": "15000.50",
          "settlementType": "2",
          "payType": "3",
          "invoiceDate": "2014-05-29",
          "invoiceContent": "4",
          "payDate": "2014-05-29",
          "htmlContent": "XHHGHHKJKKKKLGFHJRTIOOJBK...",
          "signNatureContent": "XHHGHHKJKKKKLGFHJRTIOOJBK..."
        }
a.applyDetail= [
          {
            "invoiceCode": "16612772",
            "lineItem": "10",
            "expStartDate": "2014-05-15",
            "expEndDate": "2014-05-20",
            "relationCompCode": "5400",
            "expDetail": "5",
            "settlementAmount": "7500.25"
          },
          {
            "invoiceCode": "16612773",
            "lineItem": "20",
            "expStartDate": "2014-05-15",
            "expEndDate": "2014-05-20",
            "relationCompCode": "5400",
            "expDetail": "5",
            "settlementAmount": "7500.25"
          }
        ]


try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)