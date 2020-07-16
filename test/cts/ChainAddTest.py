#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-5-30

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ChainAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.channelName='mychannel'
a.includeTraceId='111,122,2223'
a.lastMemberCode='70047381'
a.lastPoint='0111,0112'
a.lastRoleId='1'
a.memberCode='70047381'
a.memberName='苏宁'
a.msg='111'
a.point='121212'
a.roleId='1'
a.traceId='ABC96248500'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)