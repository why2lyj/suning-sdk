#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-1-9

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CmmdtypicQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cmmdtyCode='123456789'
a.picType='0:普通图，1:缩略图，2：白底图，3：透明图（白底图800*800、400*400，透明图400*400），4：主图视频'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)