#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.FmkcasdelivercouponCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityCode='SFZF20290330M011111'
a.appToken='TIvRyrNeojpnVnBk63Utga7e3'
a.appType='03'
a.buddleId='abcdef'
a.businessScene='USER_PULL_DOWN'
a.clientIp='192.168.1.1'
a.couponsAmount='1'
a.deliverSource='ECOUPON-0003'
a.egoToken='TIvRyrNeojpnVnBk63Utga7e3'
a.idNo='333333333333333333'
a.invoker='ossas'
a.memberId='1900211111'
a.pcToken='TIvRyrNeojpnVnBk63Utga7e3'
a.phoneNo='13011111111'
a.realName='你好S'
a.requestId='05257b0a296d40439a9ad212da196a84'
a.requestKey='dkjfkdj'
a.requestNo='a018ec2c289e448f8341f07eb3195a37'
a.terminalType='APP'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)