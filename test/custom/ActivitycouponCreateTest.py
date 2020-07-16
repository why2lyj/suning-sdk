#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-9-26

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ActivitycouponCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityName='店铺抽奖券'
a.activityTimesLimit='99999'
a.assignedRole='11'
a.baseAmount='999'
a.couponType='2'
a.effectEndTime='2018-09-30'
a.effectStartTime='2018-09-01'
a.endTime='2018-09-30 23:59:59'
a.rewardAmount='50'
a.shopCode='70055152'
a.startTime='2018-09-01 00:00:00'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)