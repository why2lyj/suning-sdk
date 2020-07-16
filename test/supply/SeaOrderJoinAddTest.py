#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-3-25

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SeaOrderJoinAddRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("917f0b9a93b31393cf4d4816a84c2434", "917f0b9a93b31393cf4d4816a84c2433")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.orderLineNumberList =[
          { "orderLineNumber": "1001434507" },
          { "orderLineNumber": "1001434508" }
        ]
      }

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)