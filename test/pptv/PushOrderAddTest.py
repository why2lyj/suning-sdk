#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-4-5

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PushOrderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.buyerNick='_82203a3f81a78d1292ef@alipay'
a.deliveryArea='0270702'
a.hopeArrivalTime='2016-01-01 01:01:01'
a.invoiceFlag='0'
a.invoiceName='苏宁易购'
a.invoiceType='01'
a.order=[{"discountFee":"0","payment":"520","payTypeCode":"4235","payTime":"2017-02-19 12:07:56","orderitemId":"2153","payTypeDesc":"支付宝","num":"2","totalFee":"520","price":"520","created":"2017-02-19 12:07:16","payTypeAmount":"520","numIId":"173681370","storeCode":"DZ30"}]
a.orderId='2017021912071637922761'
a.postFee='0.00'
a.receiverAddress='关山大道1号光谷软件园光谷展示中心C座5层'
a.receiverCity='武汉市'
a.receiverDistrict='洪山区'
a.receiverMobile='13995596082'
a.receiverName='姜先生'
a.receiverPhone='13995596082'
a.receiverState='湖北省'
a.receiverTown='关山街道'
a.receiverZip='223700'
a.sellerNick='pptv聚力官方商城'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)