#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-5-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CelStorageSubGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("e38f48178f9260140bb974d7949f54eb", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appointOrderId='2000017661793'
a.purchaseOrderId='1000'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)