#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-7-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.XNActivityAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("c8cc3f41c0cdfbcc6b6be6b30844866e", "8989961dc98f78578f458554dea9f486")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.activityName='test3'
a.startTime='2015-10-24 20:26:47'
a.endTime='2015-11-24 20:26:47'
a.channelInfo='31'
a.baseAmount='4'
a.rewardAmount='200'
a.isLimit='Y'
a.peopleActivityTimesLimit='5'
a.peopleDayTimesLimit='5'
a.productList=[
             {
              "productCode": "102609885"
              }
            ]


try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)