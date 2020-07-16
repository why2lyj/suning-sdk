#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-9

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.BtborderbysupplymodeCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='111111'
a.creator='张三'
a.orderDelivery={"receiverDistrict":"01","receiverDetailAddress":"苏宁大道","receiverCity":"025","receiverTown":"01","receiverMobile":"18066118801","receiverTelephone":"021-66881112","receiverProvince":"100","receiverName":"张三"}
a.orderItems=[{"cmmdtyCode":"000000000102556513","freight":"15","unitPrice":"100","supplierCode":"006644221","quantity":"1"}]
a.remark='备注'
a.storeCode='59021'
a.submitType='102'
a.supplyMode='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)