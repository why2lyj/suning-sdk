#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-4-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ResultAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.expressKey='tiantian'
a.failReason='商品已损坏'
a.freight='30.04'
a.pickupMan='张三'
a.pickupManContact='18651660535'
a.pickupNetwork='111玄武区快递点'
a.pickupNetworkContact='18651660531'
a.pickupState='0'
a.pickupTime='2017-03-27  11:34:17'
a.pushType='1'
a.returnOrderId='D201609272106001855'
a.signupState='0'
a.signupTime='2017-03-27  11:34:17'
a.waybillNo='105452777012'
a.weight='20.05'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)