#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-5-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.InventoryDetailGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("e38f48178f9260140bb974d7949f54eb", "e754e1b2da9efa2cdea1cb1873161957")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.commodityCode='100000392'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)