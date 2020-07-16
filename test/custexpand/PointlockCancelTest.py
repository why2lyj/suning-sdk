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

a=api.PointlockCancelRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.accountStruct={"uniteOrderId":"112","orderStructList":[{"store":"12","orderType":"21","orderItemId":"12","branch":"12"}],"operator":"123"}
a.appCode='11'
a.beginRecNum='0'
a.custNum='1222'
a.ecoType='111'
a.getRecNum='10'
a.sourceChannel='111'
a.sourceSystemNo='11111'
a.tranTimestamp='156000000'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)