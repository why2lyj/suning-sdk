#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-11-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='xxxx'
a.amount='88.00'
a.cityId='010'
a.companyCustNo='6114631094'
a.countyId='01'
a.email='xx@xx.com'
a.invoiceContent='1'
a.invoiceState='1'
a.invoiceTitle='11'
a.invoiceType='1'
a.mobile='xxxx'
a.orderType='0'
a.payment='01'
a.provinceId='10'
a.receiverName='张三'
a.remark='xx'
a.servFee='5.00'
a.sku=[{"num":"1","skuId":"121345091","unitPrice":"88.00"}]
a.taxNo='1234567890ABCDE'
a.telephone='010-xxxx'
a.townId='01'
a.tradeNo='1000001'
a.zip='210000'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)