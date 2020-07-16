#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-4-12

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SNServiceAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.awardFee='10.00'
a.basicFee='100.00'
a.chargbakCode='1'
a.chargbakReson='XX'
a.custName='苗苗'
a.inputFee='10.00'
a.installedId='20340304313'
a.itemGuId='4FA025393D23C08CE1008000C0A8765B'
a.longDistanceFee='20.00'
a.orderStatus='JS'
a.otherFee='3.00'
a.recordGuId='5D21BD501D63793FE1000000C0A8765D'
a.settlementId='10001023430'
a.srvOrdId='7163370425'
a.srvOrdType='ZS01'
a.telNoFir='025-66996699	'
a.telNoSec='13956443120'
a.verifyCode='103430134'
a.verifyMsg='XX错误	'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)