#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-7-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PromotionQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("cf97250875cd07d64fea3428dd3bd109", "9fb5785f3f84f60589329228182b0c0e")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.productCode='104591541'
a.pageNo='1'
a.pageSize='10'
a.startTime='2015-06-24 00:00:00'
a.endTime='2015-07-27 23:59:59'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)