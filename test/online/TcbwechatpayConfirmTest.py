#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-4-9

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.TcbwechatpayConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.tcbwechatpay={"returnUrl":"{pc:http://www.suning.com,wap:http://www.suning.com,tv:http://www.suning.com}","orderNumer":"31381068849","limitPay":"1","channelType":"1.PC ，2.微信公众号 ，3.SDK，4.TV，5.微信小程序 ，7.H5","totalAmount":"1000.10","orderItemList":[{"itemTotalAmount":"1.11","price":"1.00","orderItemNumer":"31381824805","quantity":"2"}],"merchantName":"苏宁易购商品","orderTime":"20180818081811，时间格式为:yyyyMMddHHmmss","deviceInfo":"自定义参数，可以为终端设备号(门店号或收银设备ID)，PC网页或公众号内支付可以传WEB","extraContent":"{appId:wxd678efh567hg6787,mchId:1230000109,openId:oUpF8uMuAJO_M2pxb1Q9zNjWeS6o,tradeType:JSAPI}","clientInfo":" MOBILE|01|01|5.4.1|苹果6，当channelType 传SDK时必填，联系苏宁端分配","ipAddress":"192.1.1.1"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)