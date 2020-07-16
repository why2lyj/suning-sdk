#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月3日

@author: dd
'''
import sys
sys.path.append("../../../api-sdk-python")
import suning.api

suning.setDefaultAppInfo("a494d8bb97a0d34e3e2f4caf7fa30dd8", "fcf825f1e8d605e84f4a3064fc171c2b")

a=suning.api.LogisticcompanyQueryRequest()
a.setDomainInfo("openpre.cnsuning.com","90")
#a.setAppInfo("a494d8bb97a0d34e3e2f4caf7fa30dd8", "fcf825f1e8d605e84f4a3064fc171c2b")

a.pageSize = "10"
a.pageNo= "1"

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)
