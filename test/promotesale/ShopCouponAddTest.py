#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-10-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ShopCouponAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityName='1'
a.startTime='1'
a.endTime='1'
a.activityPattern='1'
a.showRegion='1'
a.activityTimesLimit='1'
a.assignedRole='1'
a.rewardAmount='1'
a.couponType='1'
a.baseAmount='1'
a.peopleActivityTimesLimit='1'
a.effectStartTime='1'
a.effectEndTime='1'
a.channelInfo='1'
a.productRange='1'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)