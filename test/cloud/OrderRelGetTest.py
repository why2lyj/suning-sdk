#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-2-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderRelGetRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("cc473007542b03fb4bdba9191bb68415", "704242d60267d9f95c3a183f1b150fca")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.userId='6001985373'
a.itemcode='1'
a.orderId='821602241000011433'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)