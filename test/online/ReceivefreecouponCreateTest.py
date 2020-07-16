#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-8-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReceivefreecouponCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityId='201806280000391246'
a.activitySecretKey='puV2Lfm46us2NGVVFELKoOKe'
a.chanId='01'
a.city='北京市'
a.couponAmount='5'
a.couponGetSource='1001'
a.memberNo='6001858356'
a.operateType='2'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)