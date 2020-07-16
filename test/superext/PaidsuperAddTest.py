#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-4-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PaidsuperAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.amount='12.62'
a.appCode='migu'
a.externalOrderNo='8dsu8sldksjka'
a.externalUid='87sdhsjkda0923'
a.extSystemId='139000004710'
a.mixCustNum='5cbe0adc4a61447aa1ec5bca92ac52677fa5328da696492c'
a.mobileNum='13177443627'
a.payTime='20180315123655121'
a.payType='1'
a.settlementAmount='12.62'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)