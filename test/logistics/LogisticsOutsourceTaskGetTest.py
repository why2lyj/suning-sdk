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

a=api.LogisticsOutsourceTaskGetRequest()

a.logisticOrderId='2323'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)