#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-6

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ListtemplateQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.accessKeyId='1234556234'
a.accessSign='ca614d6d8289ec263462d64d5e465930'
a.appCode='234js78'
a.approved='-1'
a.code='234ACS'
a.createTimeEnd='1584429071000'
a.createTimeStart='1584429071000'
a.name='名称'
a.pageNo='1'
a.pageSize='10'
a.smsDiffer='0'
a.smsType='1'
a.status='0'
a.templateType='1'
a.timeStamp='1584429071000'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)