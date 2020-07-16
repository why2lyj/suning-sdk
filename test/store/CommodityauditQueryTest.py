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

a=api.CommodityauditQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appStoreCode='xxx'
a.auditStatus='00（00待审核  01审核通过   02审核驳回   03审核部分通过）'
a.auditType='01（01新品审核； 02修改审核；）'
a.pageNo='1'
a.pageSize='10'
a.storeCode='xxx'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)