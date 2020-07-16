#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-6-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.WareSaleQueryRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("d4d39a8040fa16d9aa499a4af9b2a660", "3fde6dadef8515ea3ecf96ae4398d5c2")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.warehouseType=''
a.pageNo='1'
a.pageSize='10'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)