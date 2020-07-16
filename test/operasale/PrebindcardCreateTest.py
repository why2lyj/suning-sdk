#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-8-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PrebindcardCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.systemNo='12'
a.transactionID='100903752018010100000000'
a.opId='10000'
a.orgId='200000'
a.regionCode='025'
a.countyCode='025'
a.channelCode='10000000'
a.phoneNumber='1709258****'
a.custName='张三'
a.idType='1'
a.idCardNum='320311********4613'
a.address='江苏省南京市xxx区xxx街道'
a.contractPhone='1709258****'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)