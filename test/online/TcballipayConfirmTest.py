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

a=api.TcballipayConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.tcbAlipay={"payTimeout":"1d","orderNumer":"31381068849","body":"苏宁易购商品","totalFee":"10001.00","channelType":"1.PC ，2.H5 ，3.SDK，4.TV，6.BDXCX（百度小程序），8.TTXCX（头条小程序）","orderItemList":[{"itemTotalFee":"10.10","orderItemNumer":"31381824805"}],"orderTime":"20180910152946，格式yyyyMMdd HHmmss","frontReturnUrl":"{pc:http://www.suning.com,wap:http://www.suning.com,tv:http://www.suning.com}","disablePaymethod":"pcredit^moneyFund或pcredit,moneyFun","clientInfo":"MOBILE|01|01|5.4.1|苹果6","goodsType":"1：实物类商品，0：虚拟类商品","enablePaymethod":"pcredit,moneyFund,debitCardExpress"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)