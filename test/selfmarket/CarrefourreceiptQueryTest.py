#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CarrefourreceiptQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.endReceivedDate='2014-04-21'
a.orderCode='1000075418_01'
a.pageNo='1'
a.pageSize='10'
a.receivedCode='5070825911'
a.startReceivedDate='2014-04-14'
a.supplierCode='10170001'
a.vendorRefNo='468887039480'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)