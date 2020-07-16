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

a=api.StatementGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a226186c2b811ce7fbce83e8a98dc7fe", "435687b33f10f5114a1d2440fe0848c7")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.confirmHead= {
        "confirmHead": {
          "supplierCode": "10001372",
          "applyCode": "17683049",
          "modelType": "1",
          "settlementType": "1",
          "settlementDate": "2014-04-02",
          "comments": "è´¹ç¨ç¡®è®¤ä»¥æç»çç« ä»¶ä¸ºå;",
          "allCheckQty": "2",
          "allCheckedAmount": "1334.70"
        }

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)