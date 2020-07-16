#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-9-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CategoryGetRequest()

a.setDomainInfo("openxgpre.cnsuning.com","80")
a.setAppInfo("0914ba076813e2004a6d067229a15196", "006280a5b7681145413cc4ba372c6a2f")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)