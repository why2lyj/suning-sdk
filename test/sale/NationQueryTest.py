#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api
'''
Created on 2014年6月5日

@author: dd
'''

a = api.NationQueryRequest()
a.nationName = u'中国'

try:
    
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)