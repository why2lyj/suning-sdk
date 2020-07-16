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

a=api.itemSaleQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.pageNo='1'
a.pageSize='10'
a.productName='女装外套'
a.productCode='102609882'
a.categoryCode='R2701002'
a.priceUpper='400.00'
a.priceLimit='50.00'
a.saleStatus='1'
a.cmTitle='夏装新款文艺棉质T恤'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)