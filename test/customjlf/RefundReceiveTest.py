#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-10-21

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.RefundReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.receiveRefundList=[{"applyRefundType":"1","cfOrderItemId":"11111222233301","reason":"退换货原因","cfOrderId":"111112222333","reasonName":"不想要了","reasonDetail":"不想要了","retNum":"12.00","applySource":"1","refundType":"1","operatMum":"家乐福"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)