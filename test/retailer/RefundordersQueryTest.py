#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-8-3

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.RefundordersQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.orderNo='00001'
a.orderItemNo='111'
a.merchantCustNo='11111'
a.storeCode='21312'
a.appId='fd3af1ads4jlg3realf5ga'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)