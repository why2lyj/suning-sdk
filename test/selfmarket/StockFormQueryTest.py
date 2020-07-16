#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-12-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.StockFormQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("4e5ffc4d6e4f714e2eaf93268cf9b8d4", "7b3360b7c9ff91c7959fe5c4c772c4da")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.placeCode='L025'
a.pageNo='1'
a.pageSize='50'
a.brandCode='000060864'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)