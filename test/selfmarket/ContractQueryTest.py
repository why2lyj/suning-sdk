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

a=api.ContractQueryRequest()

a.startTime='2014-05-04'
a.endTime='2014-05-24'
a.isSign='1'
a.supplierCode='1'
a.pageNo='1'
a.pageSize='2'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)