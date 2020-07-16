#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-1-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SeaOrderDeclareAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("d86feb368f2fcc87d11d69283ed58544", "3e1be3797982bfbf46501121cc9a43d3")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.b2cOrderNo='2003139508'
a.orderLineList= [
            {
                "orderLineNumber": "00030081246201"
            }, 
            {
                "orderLineNumber": "00030081246202"
            }
        ]
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)