#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-1-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.BoshopsrcQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='徐庄软件园92号'
a.city='025'
a.cmmdtyInfo=[{"cmmdtyCode":"89787346312","serialNumber":"89787346312","preplantCode":"89787346312","itemId":"546434313","saleNum":"5"}]
a.county='02510'
a.province='100'
a.village='0251001'
a.businessType='02'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)