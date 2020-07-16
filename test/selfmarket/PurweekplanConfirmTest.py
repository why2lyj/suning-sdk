#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-8-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PurweekplanConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.purchaseWeekPlans=[{"replenishmentQty":"1000","locationCode":"0001","weekplanStartDate":"2018M8W2","supplierConfirmTime":"2018-8-2 12:12:12","purchaseWeekPlanNo":"W000001","snProductCode":"102536103","itemStatus":"20","weekItem":"1","supplierComment":"供应商备注","plantCode":"D025"}]
a.supplierCode='1000198'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)