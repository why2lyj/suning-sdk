#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-12-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderReturnAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("9416c0de5c17023f78ea058f541f5895", "6b86c422951046e2408da57f303241b0")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.outOrderId='201512280001'
a.oldOrderId='20151228145701'
a.orderSource='201'
a.expectStartTime='2015-12-29 12:20:00'
a.expectEndTime='2015-12-29 12:20:00'
a.remark='11'
a.senderZipCode='12'
a.senderProvince='222'
a.senderCity='222'
a.senderArea='222'
a.senderTown='222'
a.senderAddress='222'
a.senderName='22'
a.senderMobile='22'
a.senderPhone='22'
a.takeFlag='2'
a.orderFlag='2'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)