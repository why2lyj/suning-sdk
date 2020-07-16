#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-4-9

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.TcborderCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.chanId='01'
a.orderId='123456789012345'
a.receiverAddress='南京玄武区梅园新村街道苏宁易购(新街口店)'
a.receiverCity='南京市'
a.receiverCounty='玄武区'
a.receiverMobile='13888888888'
a.receiverName='苏宁'
a.receiverNationality='中国'
a.receiverPhone='025-66669999'
a.receiverProvince='江苏省'
a.receiverStreet='徐庄软件园'
a.receiverZip='210000'
a.tcbOrderItemList=[{"price":"100.02","orderItemId":"123456789012345","outerSkuId":"0000000010210322","skuId":"565656565656","orderTotalFee":"100.02","saleNum":"1","postage":"0.00"}]
a.totalFee='100.02'
a.totalNo='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)