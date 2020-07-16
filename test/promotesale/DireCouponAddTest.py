#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-12-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.DireCouponAddRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("02ceb7726e47e2592d82a6472841deb2", "67e3c4355126ea68077b702554b75548")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityName='12312'
a.rewardAmount='1'
a.baseAmount='23'
a.startTime='2015-12-15'
a.endTime='2015-12-18'
a.channelInfo='1'
a.isAssign='1'
a.productList=[{ "productCode": "11" },{ "productCode": "111" }]
a.custnumList= [{ "custnum": "11" },{ "custnum": "111" }]
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)