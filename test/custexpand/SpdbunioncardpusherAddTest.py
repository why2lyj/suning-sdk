#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-7-12

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SpdbunioncardpusherAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.data='8831dfe9a08c60fa7da08536ad8bc279d754090e098eb251bb096552299f8e6ad4fc1bc6a9e924fdfa1a3d850d3cf267d3e507631fa14fa92e6e95f2feeacb8ceff69ec46ca01d92a82362aa46e63d2c65d5418db363b8c724c15fd50cd18f54f95a6fcfeb440972646f571e1ad40f2c098ed9d6def48e15c54bd148ec127d97f2f1ec5982636189373851346f95601c'
a.sign='479a2762c8f35fa3cd9f8e745d438bf9'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)