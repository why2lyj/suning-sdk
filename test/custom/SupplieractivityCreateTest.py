#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-12-12

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SupplieractivityCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.endTime='1571019600000'
a.giveAmount='11'
a.giveMaxAmount='11'
a.isNeedPhone='true'
a.levelLimit='161000000010'
a.remarks='10000|君创母婴专营店'
a.startTime='1571019600000'
a.thresholdAmount='1'
a.timesLimit='-1'
a.totalAmount='10000'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)