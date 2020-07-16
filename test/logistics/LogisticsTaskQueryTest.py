#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-8-22

@author: suning
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.LogisticsTaskQueryRequest()
a.startTime = "2014-08-05 10:24:00"
a.endTime = "2014-08-06 10:24:00"
a.pageSize = 10
a.pageNo = 1

f = a.getResponse()
print(f)
