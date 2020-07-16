#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-10-17

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.GetPriceReduceDetailRequest()

a.priceReduceId='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)