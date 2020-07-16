#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CmmdtypurchaseinfoQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='详细地址'
a.appId='111111'
a.cityCode='025'
a.cmmdtyList=[{"cmmdtyCode":"00000000063568966","itemNo":"1","quantity":"1","distributorCode":"0000000000"}]
a.districtCode='01'
a.priceDate='2020-02-11'
a.storeCode='59021'
a.townCode='99'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)