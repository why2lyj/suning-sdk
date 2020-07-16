#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api
'''
Created on 2014年6月5日

@author: dd
'''

a = api.CityQueryRequest()
a.nationCode='CN'

try:
    
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)