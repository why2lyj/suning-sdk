#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-9-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ExtensionlinkGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.productUrl='https://product.suning.com/0070204412/11046979146.html?adtype=1'
a.promotionId='fff'
a.quanUrl='https://quan.suning.com/lqzx_recommend.do?activityId=201903190001000725&activitySecretKey=kwrK5exkwqreo3QzO3GL7TSX'
a.subUser='Axxx'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)