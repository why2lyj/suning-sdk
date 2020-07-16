#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-12-13

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.BoorderCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.platFormTrade={"platFormOrder":[{"orderPayment":"123","totalFee":"523","price":"12","orderItemId":"56789001","skuId":"3456789876","serialNumber":"0023564565123","preplantCode":"D024","businessSign":"0","saleNum":"3","snSkuId":"4567899876","postage":"34"}],"payment":"100","orderType":"A001","receiverCounty":"02510","receiverMobile":"13888888888","receiverProvince":"100","businessType":"01","receiverNationality":"中国","receiverStreet":"0251001","receiverAddress":"门牌号93号","receiverCity":"025","totalNo":"2","receiverName":"苏宁","receiverZip":"8876868","orderId":"4567890","memberNo":"13888888888","receiverPhone":"1531-8295345"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)