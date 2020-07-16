#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-8-14

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReportModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.described='123'
a.fileName='123'
a.isPass='1'
a.itemCode='123456'
a.itemDesc='天然、安全、健康'
a.itemName='农夫山泉矿泉水'
a.memo='123'
a.orderDetailId='S01234567890'
a.productLink='http://product.suning.com/0000000000/10552780303.html'
a.qtCode='QT201501019876543210'
a.qtExpiry='2015-01-01'
a.qtFile='http://image.suning.cn/uimg/API/KFFW/154019177964148518.jpg'
a.qtOrderCode='S01234567890'
a.qtOrderStatus='3'
a.qtStandard='GB2001'
a.qtType='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)