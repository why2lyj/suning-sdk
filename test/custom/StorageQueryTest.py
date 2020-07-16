#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-7-5

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.StorageQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.storage=[{"billType":"01：OMS单号 02：OMS行号 03：B2C单号 04：B2C行号 返回报文时，返回对应行号","saleTaxNo":"91320106773973920L","billNo":"取单号的值（订单维度），例如：32281421244","saleOrg":"举例：70066253"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)