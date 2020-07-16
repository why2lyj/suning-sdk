#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-10-17

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.platFormTrade={"platFormOrder":[{"orderPayment":"123","totalFee":"523","price":"12","orderItemId":"56789001","outerSkuId":"4567899876","skuId":"3456789876","businessSign":"0","saleNum":"3","postage":"34"}],"payment":"100","orderType":"A001","receiverCounty":"玄武区","receiverMobile":"13888888888","receiverProvince":"江苏省","receiverNationality":"中国","receiverStreet":"徐庄软件园","receiverAddress":"门牌号93号","receiverCity":"南京市","totalNo":"2","receiverName":"苏宁","receiverZip":"8876868","orderId":"4567890","memberNo":"13888888888","receiverPhone":"1531-8295345"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)