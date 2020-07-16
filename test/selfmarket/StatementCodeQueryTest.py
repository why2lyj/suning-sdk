#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-4-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.StatementCodeQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a226186c2b811ce7fbce83e8a98dc7fe", "435687b33f10f5114a1d2440fe0848c7")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.createTimeStart='2014-04-01'
a.createTimeEnd='2014-04-14'
a.supplierCode='10001372'
a.operaType='03'
a.isSing='1'
a.isSuccess='1'
a.pageNo='1'
a.pageSize='2'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)