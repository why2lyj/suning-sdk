#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-8-22

@author: suning
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.LogisticsOrderGetRequest()
a.logisticOrderId = "SNCY0200000008059"
a.logisticExpressId = "62000000000000000001"


f = a.getResponse()
print(f)
