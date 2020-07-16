#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-2-17

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.BtborderpayinfoQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='111111'
a.appType='01'
a.channelType='PC '
a.device='apple'
a.logonUserName='小B注册登录名'
a.notifyUrl='通知URL,收银台调转URL'
a.orderNos=[{"orderNo":"A0315021214"}]
a.storeCode='59021'
a.version='V1.2'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)