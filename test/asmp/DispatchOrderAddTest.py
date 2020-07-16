#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-5-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.DispatchOrderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("5c991b791c6e5c46f925c7c6171a22cc", "911bc7ef82abc19f065f256d7afef2d9")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.orderSource='5D21BD'
a.sourceOrderItemId='12016031801704'
a.orderType='02'
a.orderTime='20160504120000'
a.saleQty='4'
a.cmmdtyQaType='0'
a.serviceTime='20160504120000'
a.extdCmmdtyBand='000010254'
a.extdCmmdtyCtgry='R0104001'
a.extdCommodityName='111'
a.consignee='11'
a.phoneNum='025-26739840'
a.mobPhoneNum='18651665787'
a.srvAddress='11'
a.standardCode='1'
a.cityCode='025'
a.srvAreaCode='0250103'
a.srvMemo='1'
a.saleDate='20160504120000'
a.serviceSource='SN'
a.salesPerson='customer'
a.orderChannel='PC'
a.faultTypeCode='1'
a.customerProperty='0001'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)