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

a=api.SspriceCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityChannel='32,36,1'
a.activityCode='操作类型为修改时，必输'
a.activityName='操作类型为新增时，必填'
a.appStoreCode='1111111'
a.endTime='操作类型为新增时，必填'
a.operationType='操作类型'
a.priceType='3=折扣；默认值3'
a.productList=[{"productCode":"1111111111","productDiscount":"1~9.99","productOperateType":"1=新增 2=修改 3=删除"}]
a.startTime='操作类型为新增时，必填'
a.storeCode='S03017113'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)