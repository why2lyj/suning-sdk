#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-24

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OtoapplyrefundCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyType='01'
a.operateTime='20180412153723'
a.orderId='12312312312'
a.orderItemIdList=[{"orderItemId":"121212212122"}]
a.orderPort='01'
a.pictureURL='www.baidu.com;www.baidu.com;www.baidu.com'
a.reasonDes='买多了'
a.reasonName='消费者不想要了'
a.retReasonCode='030'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)