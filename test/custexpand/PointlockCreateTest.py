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

a=api.PointlockCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.accountStruct={"uniteOrderId":"001168960282","orderStructList":[{"cmmdtyCode":"1","store":"11","orderItemId":"00116896028201","orderType":"11","cmmdtyBrand":"11","supplierCode":"11","cmmdtyGroup":"11","supplierType":"1","cmmdtyName":"11","accountType":"8012","branch":"11","cmmdtyCatalog":"111","orderAmt":"257.60","accountSubAmt":"22","orderTypeDesc":"11"}],"operator":"OMS"}
a.appCode='mos'
a.beginRecNum='0'
a.custNum='6187218898'
a.ecoType='140000000010'
a.getRecNum='10'
a.sourceChannel='11'
a.sourceSystemNo='11'
a.tranTimestamp='1562862504858'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)