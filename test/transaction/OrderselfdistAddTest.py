#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-9-25

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderselfdistAddRequest()

a.orderCode='111'
a.deliveryPerName='222'
a.deliveryPerPhone='13565845784'
a.deliveryTime='2014-12-12 14:10:20'
a.productCodes={"productCode":["102609881"]}
a.orderLineNumbers={"orderLineNumber":["100151521"]}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)