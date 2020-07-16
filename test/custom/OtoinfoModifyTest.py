#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-9-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OtoinfoModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.autoRefund='0'
a.bookingShop='0'
a.childItem=[{"priceChild":"1.00","deductiblePriceChild":"1.00","productCodeChild":"1000000000"}]
a.deductiblePrice='1.00'
a.effectiveDay='99'
a.extractMode='01,10'
a.insaleRefund='0'
a.payTemplate='1'
a.price='1.00'
a.priceType='01'
a.productCode='1'
a.saleDate='2013-10-1'
a.saleSet='0'
a.sellChannel='01'
a.writeoffPayment='0'
a.writeoffShop='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)