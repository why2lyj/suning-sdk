#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-6-21

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderCouponAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("97df3d2ad61f460a78bce2be41497268", "a73d0e4436b606b5d1ad69d5677fff9a")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityName='11'
a.startTime='2016-06-22 00:00:00'
a.endTime='2016-06-22 00:00:00'
a.channelInfo='31'
a.activityProductType='1'
a.couponProductType='1'
a.returnCouponType='1'
a.returnCouponValue='1'
a.activityLimit='1'
a.activityTimesLimit='1'
a.peopleActivityTimesLimit='1'
a.effectDays='1'
a.baseQuantifierType='1'
a.rewardType='1'
a.areaCode='1'
a.booleanCap='1'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)