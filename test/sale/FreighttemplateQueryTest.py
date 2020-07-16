#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api
'''
Created on 2014年6月5日
suning.custom.freighttemplate.query批量查询运费模板
@author: dd
'''

a = api.FreighttemplateQueryRequest()
a.pageNo = 1
a.pageSize = 20

try:
    
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)