#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-10-18

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.MvstockReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.deliNumber='123456'
a.deliType='ZVIN'
a.soCreatDate='20191010'
a.soCreatTime='110120'
a.cmmdtyMvStockInfoList=[{"commodityDes":"123456","taskLinage":"123456","stockAreab":"0001","stockAreaa":"0001","provideAddressa":"ZE99","provideAddressb":"ZE99","taskNumber":"123456","deliSort":"ELN","commodityCode":"123456","deliNum":"1"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)