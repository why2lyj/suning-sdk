#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-12-18

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.GetLogisticsCrossbuyPrdCustDeclRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("7671c52d74ce85fde1d219c7ad9d2c81","c87d119d63660e4d6372f07a42d2e4e5")

a.logisticOrderId=''
a.orderNo='111'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)