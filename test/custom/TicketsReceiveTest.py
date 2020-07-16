#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-10-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.TicketsReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.failedCode='E001'
a.failedReason='订单不存在'
a.orderCode='苏宁订单号'
a.orderItemCode='20180930001'
a.orderStatus='1'
a.successTime='2018-09-03 00:00:00'
a.ticketList=[{"pdfCode":"19445","additional":"1123456","qrCode":"11213554","serialCode":"xxxxyyyyyzz"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)