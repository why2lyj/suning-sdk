#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-8-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SupplierplanAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.dataList=[{"weekEndDate":"2019/7/17","plantName":"南京仓","productCode":"102536103","weekPlanDate":"2018M8W2","snProductCode":"124521","purchaseQty":"100","weekPlanNo":"W000000001","planCreateDate":"2019/7/17","weekStartDate":"2019/7/17","productName":"海信空调","plantCode":"D025"}]
a.supplierCode='10000197'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)