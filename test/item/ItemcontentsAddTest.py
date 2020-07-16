#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月4日

@author: 14050313
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api 

a=suning.api.ItemcontentsAddRequest()
a.afterSaleServiceDec = "好的售后服务"
a.freightTemplateId = "9d2371d9bbd44a078a2e466a04f68734"
a.introduction = "5rWL6K+V5ZWG5ZOB5LuL57uN"
a.invQty = "1"
a.price = "10.0"
a.productCode = "108330798"
a.saleDate = "2014-06-23"
a.saleSet = '0'
a.sellPoint = '好的测试商品'
try:
    print(a.getApiContent())
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)


    
