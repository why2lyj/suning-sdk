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

a=api.AppstoreUpdateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appStoreCode='asdf12312'
a.branchStoreName='XX分店'
a.custNum='7018048766'
a.dayHours='07:00-12：00#14:00-21:00'
a.latitude='34.82984'
a.longitude='113.683856'
a.openDay='01#02'
a.storeAdd='格式不限，长度5-80汉字'
a.storeArea='02501'
a.storeCode='S03017159'
a.storeCondues='最大500汉字'
a.storeContact='人名'
a.storeDeliveryMode='0'
a.storeInCity='025'
a.storeInProVince='100'
a.storeLogo='https://uimgpre.cnsuning.com/uimg/sop/commodity/232883071680181112790000_x.jpg'
a.storeName='XX门店'
a.storePict='http://uimgpre.cnsuning.com/uimg/sop/commodity/210767194810691023962395_x.png'
a.storeStatus='0'
a.storeTel='13800000000'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)