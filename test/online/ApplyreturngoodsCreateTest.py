#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-7-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ApplyreturngoodsCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyType='01'
a.attachInfo='N'
a.orderId='2016092815103015'
a.orderItemId='100201609281506100005002'
a.orderStatus='06'
a.packInfo='N'
a.picInfo=[{"picture":"www.baidu.com"}]
a.reOrderItemId='123456789'
a.retDesc='退货说明'
a.retNum='10.00'
a.retReason='1'
a.useInfo='N'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)