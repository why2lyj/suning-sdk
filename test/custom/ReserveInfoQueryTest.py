#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-2-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReserveInfoQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.actionId='201912090011'
a.snUnionId='bfb3ae009a31e98f4fa13ee41c6cbfb3ae01f9a31e9884fa'
a.partnumber='000000000761102589'
a.beginTime='2012-04-25 20:23:30'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)