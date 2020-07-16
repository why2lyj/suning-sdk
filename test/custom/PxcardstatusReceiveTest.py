#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-6-26

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PxcardstatusReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='XX省XX市XX区XX地方'
a.deliveryDate='2020-05-26 17:00:00'
a.expressCompanyCode='顺丰物流'
a.expressNo='SF9994588556'
a.name='XXX'
a.orderItemId='00120485973301'
a.phoneNum='02588888888'
a.pickupMode='1'
a.pxCardId='10000011'
a.pxCardNo='22223334'
a.pxCardStatus='01'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)