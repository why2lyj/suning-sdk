#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-9-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.StoreAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.branchStoreName='新街口店'
a.dayHours='07:00-19:00'
a.latitude='34.82984'
a.longitude='113.683856'
a.ownstoreCode='长度0-50位汉字'
a.storeAdd='南京徐庄软件园苏宁易购总部'
a.storeArea='02501'
a.storeCondues='最大500汉字'
a.storeName='苏宁易购门店'
a.storeInProVince='100'
a.storeInCity='025'
a.storeTel='0731-83521795,18512580194,025-66778899'
a.storeStatus='1'
a.storePict='https://uimgpre.cnsuning.com/uimg/sop/commodity/129309315134056997373040.png'
a.storeEpp='15861804398'
a.storeEppPayFlag='Y'
a.storeEppPay='15861804398'
a.storeSend='Y'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)