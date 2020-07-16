#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-22

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ShoppingcartCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.chan='1'
a.cmmdtyCode='11761222626'
a.cmmdtyName='xxx'
a.cmmdtyQty='1'
a.operationEquipment='01'
a.operationTerminal='01'
a.overSeasFlag='927HWG1'
a.snUnionId='243465676878'
a.tickStatus='0'
a.xzActivityId='20032412072321366607'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)