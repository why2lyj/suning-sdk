#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-5-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ExpenseorderConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.detail=[{"blanceQty":"2","blanceSalesAmount":"100","relatedShop":"7153","relatedWareHouse":"D025","blanceAmount":"100.10","itemCode":"625173988"}]
a.head={"settlementDate":"2018-10-01","settlementType":"1","operateType":"1","modelType":"1","supplierCheckAmount":"100.01，","supplierCode":"10000001","applyCode":"70891182","comments":"修改金额。","supplierCheckQty":"1"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)