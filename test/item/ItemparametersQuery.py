#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api
'''
Created on 2014年6月5日
suning.custom.itemparameters.query获取商品参数模板
@author: dd
'''

a = api.ItemparametersQueryRequest()
a.categoryCode = 'R5101006'
a.pageSize = 20
a.pageNo = 1

try:
    
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)