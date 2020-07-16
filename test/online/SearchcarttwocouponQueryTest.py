#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-1-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SearchcarttwocouponQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cartTwoNo='242225492431967067'
a.chanId='02'
a.city='北京市'
a.mainProductList=[{"cmmdtyCode":"000000010533645636","price":"100.00","itemId":"252225492431458174","discountList":[{"activityType":"5","discount":"100.00"}],"businessSign":"0","saleNum":"12","marketingActivityType":"0"}]
a.memberNo='6207320981'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)