#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-3-21

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.SspriceQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityName='418大促活动'
a.activityStatus='空：全部 s01:处理中 s02:待开始 s03:进行中 s04:已终止 s05:已结束 s09:即将结束'
a.appStoreCode='1111111111'
a.pageNo='1'
a.pageSize='10'
a.storeCode='S03017113'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)