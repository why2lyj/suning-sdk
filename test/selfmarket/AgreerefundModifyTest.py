#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-2-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.AgreerefundModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.omsOrderItemNo='00004849094302'
a.supplierCode='70060534'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)