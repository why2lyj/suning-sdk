#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-4-20

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ProductsearchQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.aggregate='1'
a.attrList='111'
a.brandId='0IAC'
a.categoryIdOne='1111'
a.categoryIdThree='11'
a.categoryIdTwo='11'
a.cityCode='025'
a.limit='200'
a.max='200'
a.min='100'
a.page='1'
a.searchContent='惠普打印机'
a.sortType='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)