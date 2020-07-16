#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-4-20

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.FactoryServiceAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("82fdfb8aa13d18b1b3fd703b02f5d45e", "f73e8c8b9a0ef3b29a408fb71274edbd")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.recordGuId='1'
a.itemGuId='1'
a.srvOrdId='1'
a.srvOrdType='1'
a.orderStatus='1'
a.facSiteName='1'
a.facSiteTel='1'
a.srvStatus='1'
a.inCompleteReason='1'
a.installedId='1'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)