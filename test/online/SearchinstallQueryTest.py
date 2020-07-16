#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-7-12

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SearchinstallQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='XXX小区XXX号'
a.chanId='02'
a.city='南京市'
a.cmmdtyCode='000000000102423671'
a.county='江宁区'
a.orderItemId='99883884'
a.province='江苏省'
a.saleNum='2'
a.selectedArrivalTime='2018-08-24-1'
a.village='淳化镇'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)