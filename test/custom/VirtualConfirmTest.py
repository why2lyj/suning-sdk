#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-6-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.VirtualConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cardList=[{"cardCode":"1234567899","cardSec":"I001XB999"}]
a.dealResult='T'
a.failedCode='FAIL0'
a.failedReason='卡号密码不正确'
a.goodsSnap='URL'
a.orderCode='10000011'
a.orderItemCode='00120485973301'
a.successTime='2018-01-01 00:01:01 '

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)