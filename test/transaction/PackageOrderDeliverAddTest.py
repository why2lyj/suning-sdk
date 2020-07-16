#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-10-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PackageOrderDeliverAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("927b8dabc68dbdc5c778892bd811ea87", "894aa4ed1010409e9ec50deddf80f250")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.packageOrderId='00000000100005502363'
a.deliveryType='02'
a.expressCompanyCode='B01'
a.expressNo='123123'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)