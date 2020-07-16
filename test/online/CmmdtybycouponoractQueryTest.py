#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-2-20

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CmmdtybycouponoractQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityId='1234567123'
a.chanId='01'
a.city='南京市'
a.couponRuleId='1201805290001422385'
a.cp='0'
a.kw='手机'
a.price='0_888'
a.ps='60'
a.snfw='1'
a.st='0'
a.stock='0'
a.type='0'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)