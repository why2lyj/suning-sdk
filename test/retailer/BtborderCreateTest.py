#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-7-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.BtborderCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='666666'
a.channelCode='19541'
a.orderDelivery={"districtCode":"01","provinceCode":"100","cityCode":"025","receiverName":"张三","buyerAddress":"江苏省南京市玄武区玄武大道1号","townCode":"01","receiverPhone":"18632486868"}
a.orderInvoice={"invoiceTitleType":"1","invoiceReceiverPhone":"135889088765","invoiceType":"1","invoiceReceiverName":"张三","invoiceAddress":"江苏省南京市玄武区玄武大道1号","taxPayerNo":"122021154545x","invoiceTitle":"个人"}
a.orderItemList=[{"cmmdtyCode":"000000000102556513","price":"2000.00","itemTotalFare":"24.00","serviceCmmdtyCode":"000000000102556513","hopeArrivalTime":"2018-08-30","quantity":"1","bookTimeDetail":"2018-07-01","outerOrderItemNo":"B20190505180001021","installFlag":"0","distributorCode":"0000000000"}]
a.outerOrderNo='B2019050518000801'
a.payWay='9'
a.remark='备注信息'
a.storeCode='59021'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)