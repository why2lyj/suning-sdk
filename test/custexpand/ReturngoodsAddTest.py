#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReturngoodsAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.addStructList=[{"accountType":"accountType1","accountAddAmt":"accountAddAmt"}]
a.appCode='appCode'
a.backOrderItemId='backOrderItemId'
a.branch='branch'
a.custNum='custNum'
a.ecoType='ecoType'
a.handlers='handlers'
a.isCalcTotalOffsetLimit='isCalcTotalOffsetLimit'
a.onLineFlag='onLineFlag'
a.orderItemId='orderItemId'
a.orderType='orderType'
a.returnScene='returnScene'
a.sourceChannel='sourceChannel'
a.sourceSystemNo='sourceSystemNo'
a.store='store'
a.subtractStructList=[{"accountTp":"accountTp","accountSubAmt":"accountSubAmt"}]
a.tranTimestamp='tranTimestamp'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)