#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-8-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PriceExclusiveModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityCode='1234567896'
a.createWay='1'
a.activityName='万人空巷强空调'
a.startTime='2016-08-25 11:23:35'
a.endTime='2016-08-25 11:23:35'
a.channelInfo='1'
a.priceType='1'
a.productList=[{"productCode":"140038448","childList":[{"operationType":"1","priceAmount":"1","subProductCode":"1111"}],"cmType":"01"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)