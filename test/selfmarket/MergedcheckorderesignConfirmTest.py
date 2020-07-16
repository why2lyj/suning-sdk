#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-5-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.MergedcheckorderesignConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.head={"settlementDate":"2018-10-01","signDate":"2018-10-01","settlementType":"1","signNatureContent":"ENCODE:UTF-8","modelType":"1","supplierCheckOrderCode":"DMSH11033101","supplierCode":"10000001","comments":"确认费用","htmlContent":"ENCODE:UTF-8"}
a.checkOrderList=[{"applicationCode":"5400X0011905002937","applyCode":"70861323"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)