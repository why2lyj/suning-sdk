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

a=api.PointsubtractConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.accountStruct={"uniteOrderId":"11","orderStructList":[{"cmmdtyCode":"11","subtractStructList":[{"accountType":"11","accountSubAmt":"12.30"}],"store":"11","orderItemId":"11","orderType":"11","cmmdtyBrand":"12","supplierCode":"11","cmmdtyGroup":"11","supplierType":"11","cmmdtyName":"12","branch":"11","cmmdtyCatalog":"11","orderAmt":"254.60","orderTypeDesc":"11"}],"operator":"11"}
a.appCode='oms'
a.beginRecNum='0'
a.custNum='11'
a.ecoType='11'
a.getRecNum='1'
a.sourceChannel='113.194.18.7'
a.sourceSystemNo='139000000070'
a.tranTimestamp='1562862504858'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)