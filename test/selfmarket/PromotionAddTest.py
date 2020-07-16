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

a=api.PromotionAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a226186c2b811ce7fbce83e8a98dc7fe", "435687b33f10f5114a1d2440fe0848c7")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.supplierCode='10001372'
a.supplierBraComp='SEBJ'
a.supplierOffice='1'
a.snCode='5400'
a.supplierApplicationCode='FYBJ14061004'
a.productBrand='0123,0124,0125'
a.expenseBudgetCode='123456789'
a.areaCopCode='1001'
a.startDate='2014-05-19'
a.endDate='2014-05-29'
a.promotActivName='1'
a.promotAgreementName='1'
a.paymentLittleMount='10000.60'
a.settlementType='1'
a.invoiceDate='2014-05-29'
a.payType='3'
a.invoiceContent='2'
a.payDate='2014-05-29'
a.htmlContent='XHHGHHKJKKKKLGFHJRTIOOJBK...'
a.signNatureContent='XHHGHHKJKKKKLGFHJRTIOOJBK...'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)