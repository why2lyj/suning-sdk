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

a=api.SearchcartonecouponQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.chanId='01'
a.city='北京市'
a.mainProductList=[{"cmmdtyCode":"000000000729750740","price":"699.00","itemId":"570325383766595145","discountList":[{"activityType":"5","discount":"100.00"}],"businessSign":"0","saleNum":"1","marketingActivityType":"4-1"}]
a.memberNo='7018181818'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)