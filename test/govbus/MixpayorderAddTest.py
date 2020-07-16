#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-3-10

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.MixpayorderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='江苏省南京市雨花区软件大道舜天集团'
a.amount='88.00'
a.cityId='025'
a.companyCustNo='15114631094'
a.countyId='05'
a.email='xxx@xxx.com'
a.hopeArrivalTime='2019-11-06-3'
a.invoiceContent='1'
a.invoiceState='1'
a.invoiceTitle='江苏舜天有限公司'
a.invoiceType='1'
a.mobile='15311351111'
a.orderType='1'
a.payment='08'
a.provinceId='100'
a.receiverName='张三'
a.remark='xxxxx'
a.servFee='5.00'
a.sku=[{"num":"1","skuId":"140272356","unitPrice":"88.00"}]
a.specialVatTicket={"taxNo":"1234567890ABCDE","consigneeName":"张三","regTel":"18767890345","consigneeAddress":"江苏省南京市秦淮区法院","regAdd":"江苏省南京市雨花区软件大道舜天集团","regAccount":"23235254664336","companyName":"江苏舜天有限公司","regBank":"453453434534354","consigneeMobileNum":"15822222200"}
a.subPaymentModes=[{"payAmount":"50","payCode":"7207"}]
a.telephone='010-84728989'
a.townId='01'
a.tradeNo='1000001'
a.zip='210000'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)