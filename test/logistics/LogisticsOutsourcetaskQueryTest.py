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

a=api.LogisticsOutsourcetaskQueryRequest()

a.startTime='2014-05-05 10:20:30'
a.endTime='2014-05-06 10:20:30'
a.pageSize='10'
a.pageNo='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)