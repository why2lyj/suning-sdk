#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-10-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.UnionInfomationQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("49b99e6f6e4ac8038e4f189497cb625c", "3f593ad4101d6533ea447a20f1f4b8de")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.pageNo='1'
a.pageSize='10'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)