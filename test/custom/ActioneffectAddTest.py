#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-7-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ActioneffectAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityId='20050516554033782968'
a.memberId='6227757192'
a.profitValue='10'
a.actionType='102'
a.statisTime='2020-02-02 18:00:00'
a.snUnionId='5232db605f31ea8f0fa13eeda5da5232db6155f31ea800fa'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)