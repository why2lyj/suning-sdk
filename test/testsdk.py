#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-2-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api.custom as api

a=api.ActivityGetRequest()

a.setDomainInfo("opensit.cnsuning.com","80")
a.setAppInfo("fadb2d37f26aba072bc0295b47013692", "59521d43f9f563df9bf80bb723eafcbe")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityId='20032620140316961395'
a.setPointParams({"testsdkid":"202004081509"})
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)