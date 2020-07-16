#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-1-12

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.orderSelfDistAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.deliveryPerName='张三'
a.deliveryPerPhone='13899995555'
a.deliveryTime='2012-06-20 00:00:00'
a.orderCode='88888'
a.orderLineNumbers={"orderLineNumber":"100151521"}
a.phoneIdentifyCodes=[{"phoneIdentifyCode":"1","productCode":"1","orderLineNumber":"1"}]
a.productCodes={"productCode":"108252389"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)