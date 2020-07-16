#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-1-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.IntegralCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityName='20200101店铺积分兑换'
a.endTime='2020-01-01 00:00:00'
a.integralRwardInfos=[{"rewardDesc":"国行正品","picUrl":"//image.suning.cn/uimg/mpms/promotion/152026760052716646.jpg","totalBudgetCount":"100","rewardName":"iP8","exchangeCount":"2","customersCode":"1000000010","memDayAllLimit":"22","consumeIntegral":"100"}]
a.shopCode='300009484'
a.startTime='2019-01-29 01:02:02'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)