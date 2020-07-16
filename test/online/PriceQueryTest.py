#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-12-20

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PriceQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cmmdtyInfo=[{"cmmdtyCode":"123456789","village":"淳化镇","orderItemId":"99883884","county":"江宁区","address":"XXX小区XXX号","chanId":"02","province":"江苏省","saleNum":"2","city":"南京市"}]
a.sceneType='1:列表搜索 2:详情页面 3:购物流程'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)