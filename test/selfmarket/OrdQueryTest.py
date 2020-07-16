#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrdQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.endTime='yyyy-MM-dd HH:mm:ss'
a.orderItemStatus='订单行状态,10:待发货,40:已发货,45:已代顾客确认收货,50:顾客已收货,60:单证已寄票,70:顾客已收票,75:交易关闭'
a.pageNo='1'
a.pageSize='10'
a.startTime='yyyy-MM-dd HH:mm:ss'
a.supplierCode='123456789'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)