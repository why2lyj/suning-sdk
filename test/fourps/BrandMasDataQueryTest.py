#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-2-23

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.BrandMasDataQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("9416c0de5c17023f78ea058f541f5895", "6b86c422951046e2408da57f303241b0")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.brandName='æµ·'
a.pageNo='1'
a.pageSize='5'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)