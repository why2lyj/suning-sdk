#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-5-4

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderEvaluateGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("2238a6ccacf472caba35aaa92610983a", "83505555d41533459d74305c0a68acd3")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.orderCode='1003163008'
a.productCode='150011381'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)