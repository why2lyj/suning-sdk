#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-3-21

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderdiscountsideCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityName='中文zimu@#￥'
a.allShopType='0'
a.appStoreCode='S03017113'
a.baseQuantifierType='1'
a.channelInfo='55,56'
a.endTime='2019-03-04 20:25:59'
a.productList=[{"productCode":"761134378"}]
a.rewardQuantifierType='1'
a.ruleList=[{"baseAmount":"9999","rewardAmount":"999"}]
a.startTime='2019-03-04 20:23:00'
a.storeCode='S03017113'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)