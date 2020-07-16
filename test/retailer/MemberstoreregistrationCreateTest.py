#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-7-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.MemberstoreregistrationCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='666666'
a.channelCode='19451'
a.cityCode='025'
a.cityName='025'
a.companyAddr='苏宁大道1号'
a.companyName='公司名称'
a.companyType='1'
a.contactPerson='张三'
a.contactPhone='02566783636'
a.districtCode='01'
a.districtName='玄武区'
a.legalIdcardNo='3402106197812023678'
a.legalPerson='张三'
a.licenseNo='6652841194'
a.merchantType='0'
a.provCode='100'
a.provName='江苏省'
a.townCode='01'
a.townName='主城区'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)