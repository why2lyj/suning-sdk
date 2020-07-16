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

a=api.XNActivityModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("cf97250875cd07d64fea3428dd3bd109", "9fb5785f3f84f60589329228182b0c0e")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")

a.activityCode='15072712062310000005'
a.startTime='2015-09-01 16:36:00'
a.endTime='2015-09-03 16:36:00'
a.baseAmount='3'
a.rewardAmount='100'
a.isLimit='N'
a.productList=[
             {
              "productCode": "122028287",
"operateFlag": "1"
              }
            ]


try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)