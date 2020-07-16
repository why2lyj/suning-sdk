#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-8-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CarttwoactandcouponConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cartTwoNo='123'
a.chanId='01'
a.city='南京市'
a.couponUsedList=[{"couponNumber":"010134715354"}]
a.mainProductList=[{"cmmdtyCode":"000013431234512345","price":"1.00","itemId":"12345671334","businessSign":"0","saleNum":"2","marketingActivityType":"4-1"}]
a.memberNo='18397652345'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)