#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-12-13

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.IdentifyresultConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.isAll='1'
a.serialList=[{"itemNo":"1","serialNum":"B000001","blpList":[{"imperfectProjectList":[{"imperfectProjectValue":"01","imperfectProjectNo":"1"}],"basicProjecList":[{"basicProjecValue":"01","basicProjecNo":"1"}],"updateTime":"2019-11-26 00:00:00","abnormalReport":"00","imperfectGrade":"S","viewNum":"0010"}]}]
a.tripCode='SFJD0000000515'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)