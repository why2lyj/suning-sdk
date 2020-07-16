#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-3-5

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ElectronicInvoiceAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.invoiceAmount='开票合计金额'
a.invoiceCode='1111'
a.invoiceData='13v1123v3bh2h234'
a.invoiceFlag='02'
a.invoiceHead='苏宁易购'
a.invoiceHeadType='1'
a.invoiceNo='1111'
a.invoiceNoTaxAmount='不含税金额'
a.invoiceSecurityCode='59888 37763 38108 76652'
a.invoiceTime='2016-08-01 10:10:10'
a.invoiceType='1'
a.logisticsComp='纸质发票存在物流公司'
a.logisticsOrderId='纸质发票存在物流单号'
a.oldInvoiceCode='1234'
a.oldInvoiceNum='123'
a.orderId='4511680451'
a.productCode='1111'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)