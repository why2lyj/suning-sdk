#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-3-31

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.DeliverynewAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.deliveryTime='2012-06-20 00:00:00'
a.expressCompanyCode='B01'
a.expressNo='B030103'
a.orderCode='4511680451'
a.orderLineNumbers=[{"productCode":"108252389","orderLineNumber":"100151521"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)