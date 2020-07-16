#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-1-12

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ChilditemAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.parentProductCode='1000'
a.pars=[{"parCode":"1000","parValue":"子商品特性参数值"}]
a.supplierImgAUrl='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.itemCode='123'
a.barcode='123'
a.barpic='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)