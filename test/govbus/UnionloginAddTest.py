#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-11-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.UnionloginAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.catalog='A0205'
a.channel='1'
a.comabb='ALi'
a.comName='阿里巴巴公司'
a.extra='待定'
a.limit='100'
a.limitEndDate='2019-05-02'
a.limitStartDate='2019-05-01'
a.limitType='1'
a.role='2,3,4,5'
a.spUid='A001'
a.sysCode='145000004094'
a.targetUrl='www.suning.com'
a.uid='yqg85984541'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)