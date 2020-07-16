#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-13

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SignatureAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.accessKeyId='1234736185885548544'
a.accessSign='e6a73a692e8235cf23c576d4dc4db6db'
a.businessLincenseFileContent='212h97qwg'
a.businessLincenseFileSuffix='jpg'
a.certificateType='0'
a.name='苏宁'
a.orgCodeFileContent='2huhd2q1123wsa'
a.orgCodeFileSuffix='jpg'
a.remark='签名自用'
a.screenshotFileContent='26389306gs5'
a.screenshotFileSuffix='jpg'
a.sourceName='0'
a.subject='0'
a.taxationFileContent='2323rds25rsd'
a.taxationFileSuffix='jpg'
a.threeInOneFileContent='121ee4df4f436'
a.threeInOneFileSuffix='jpg'
a.timeStamp='1584414239000'
a.userId='701248376'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)