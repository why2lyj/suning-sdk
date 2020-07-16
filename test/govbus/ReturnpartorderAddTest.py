#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-2

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReturnpartorderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.aftersaleAddress={"provinceId":"01","cityId":"010","address":"广顺北大街21号院108楼208室","townId":"0100102","countyId":"01001"}
a.aftersaleName='李*'
a.aftersalePhone='13333333333'
a.bankName='01'
a.cardNumber='1000406047888888'
a.cardUsername='张**'
a.orderId='100000100025'
a.skus=[{"num":"2","reason":"0101","skuId":"121345077","reasonDetails":"退货"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)