#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-3-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.IssueinvoicesrcdomsCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='appId'
a.invoiceIssueReqDTO={"regTel":"11","receiveTel":"11","cityCode":"11","invoiceType":"1","snCustNum":"11","regAddr":"11","companyName":"11","invoiceTitle":"11","townCode":"11","taxNo":"11","districtCode":"11","regAccount":"11","receiveName":"11","provCode":"11","receiveAddr":"11","regBank":"1111"}
a.respList=[{"omsOrderItemNo":"11"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)