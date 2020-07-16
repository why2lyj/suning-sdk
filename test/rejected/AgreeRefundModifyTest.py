#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-2-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.AgreeRefundModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("f9ebbfe7100e089b18c1f85513e74678", "03e372c1b0c9a2440844740262cf1dd4")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.childAccountName='soppre12345@163.com'
a.code='324713'
a.orderItemId='00030081505202'
a.returnMoney='107'
a.applyTime='2016-02-23 19:10:23'
a.returnType='4'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)