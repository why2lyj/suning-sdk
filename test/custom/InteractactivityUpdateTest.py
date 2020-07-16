#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-18

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.InteractactivityUpdateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityDes='测试活动描述'
a.activityId='20032411275626277214'
a.activityName='测试活动'
a.activityType='1'
a.endTime='2020-02-16 18:23:06'
a.startTime='2020-02-15 18:23:06'
a.storeCodes='78694881,78694882'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)