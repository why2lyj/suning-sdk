#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderbuyConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cardType='cardType'
a.custNum='custNum'
a.deviceId='deviceId'
a.ecoType='ecoType'
a.invokerCode='调用方编码'
a.orderId='orderId'
a.orderItem=[{"giftCardMoney":"giftCardMoney","store":"store","stockArea":"stockArea","cmdtyName":"cmdtyName","orderItemId":"orderItemId","cmdtyCode":"cmdtyCode","payItem":[{"payMoney":"payMoney","payMode":"payMode"}],"orderItemType":"orderItemType","payTime":"payTime","transportFee":"transportFee","couponTotalMoney":"couponTotalMoney","cmdtyBrand":"cmdtyBrand","cmdtyCatalog":"cmdtyCatalog","orderAmt":"orderAmt","orderTypeDesc":"orderTypeDesc","distChannel":"distChannel","dealItem":[{"dealTypeFlag":"dealTypeFlag","promotionNum":"promotionNum","dealType":"dealType"}],"serviceFee":"serviceFee","purchaseFlag":"purchaseFlag","pointMoney":"pointMoney","orderType":"orderType","invoiceType":"invoiceType","supplierCode":"supplierCode","cmdtyCount":"cmdtyCount","supplierType":"supplierType","branch":"branch","managerCardMoney":"managerCardMoney","staffNum":"staffNum","cmdtyGroup":"cmdtyGroup","activityType":"activityType"}]
a.orderSubmitTime='orderSubmitTime'
a.sceneType='sceneType'
a.transId='transId'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)