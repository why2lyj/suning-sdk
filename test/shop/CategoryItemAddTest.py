#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-8-22

@author: suning
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.ShopCategoryItemAddRequest()
a.categoryCode = "100001"
a.products = {"productCode":["108294258","208294666"]}

f = a.getResponse()
print(f)
