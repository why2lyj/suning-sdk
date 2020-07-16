#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.LogisticsCrossbuyInvModifyRequest()

a.warehouseCode='L009'
a.productInv={"productInv":[
 				{
 					"cargoOwner":"R5400",
 					"deadlineDate":"20181231",
 					"productCode":"901030591",
 					"productName":"IPHON6",
 					"restrictedStock":"100",
 					"unrestrictedStock":"100",
 					"useStock":"100"
 				}]}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)