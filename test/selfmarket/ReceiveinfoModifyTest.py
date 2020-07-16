#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-1-12

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ReceiveinfoModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cityName='南京市'
a.customerName='张三'
a.detailAddress='苏宁大道1号'
a.districtName='玄武区'
a.mobilePhoneNum='1110002222'
a.orderCode='101030001'
a.phoneNum='02566996699'
a.provinceName='江苏省'
a.supplierCode='10001373'
a.townCode='0250101'
a.townName='仙鹤门街道'
a.userName='aa@163.com'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)