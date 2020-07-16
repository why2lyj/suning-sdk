#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-4-1

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PushRefundAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.buyerNick='tbtest561'
a.companyName='申通快递'
a.createdTime='2016-01-01 00:00:00'
a.desc='测试'
a.modifiedTime='2016-01-02 00:00:00'
a.num='1'
a.oid='1377744083656645'
a.orderStatus='TRADE_BUYER_SIGNED'
a.outerId='ISBN-001'
a.reason='测试'
a.refundFee='10.00'
a.refundId='54479739429405'
a.refundNum='1'
a.refundPhase='onsale'
a.refundVersion='1411375308927'
a.sellerNick='tbtest869'
a.sid='123456789'
a.status='SELLER_REFUSE_BUYER'
a.tid='1377744083656645'
a.title='天堂伞龙井茶'
a.totalFee='10.00'
a.type='T'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)