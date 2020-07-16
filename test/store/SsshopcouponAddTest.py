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

a=api.SsshopcouponAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityEndTime='到分 2018-01-01 00:00'
a.activityName='618大促发券活动'
a.activityStartTime='到分，2018-01-01 00:00'
a.appStoreCode='1111111'
a.baseAmount='正整数1~999999999'
a.baseQuantifierType='1:满'
a.circulation='正整数:1~999999999'
a.couponType='1:店铺易券'
a.denomination='正整数 1~3000'
a.dynamicDistanceTimeDelay='整数：0~90'
a.dynamicTime='整数：0~90'
a.effectiveEndTime='到分钟2018-01-01 00:00'
a.effectiveStartTime='到分 2018-01-01 00:00'
a.grantCountEveryday='正整数'
a.limitCollarCount='0：不限  1:一张 2：二张 3：三张 4：四张 5：五张'
a.limitCollarEveyDay='0：不限  1:一张 2：二张 3：三张 4：四张 5：五张'
a.shopCode='S03017113'
a.showRegion='1,8'
a.useChannelStr='多个以逗号隔开 55,56,57'
a.validityType=' 1:固定时间 2：动态时间'
a.voucheObject='1：不限'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)