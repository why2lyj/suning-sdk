#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-6-25

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ApplyrepairgoodsCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='望京东路8号'
a.cityId='025'
a.countyId='01'
a.mobPhoneNum='13088888888'
a.num='1'
a.orderId='1418628119786'
a.orderItemId='141862811978601'
a.orderMemo='洗衣机滚筒电机损坏'
a.phoneNum='010-88888888'
a.provinceId='12'
a.receiverName='张三'
a.serviceTime='20180101180000'
a.skuId='3454343545'
a.srvMemo='带一根1米长水管'
a.townId='90'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)