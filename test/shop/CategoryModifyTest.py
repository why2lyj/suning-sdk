#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-8-22

@author: suning
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.ShopCategoryModifyRequest()
a.shopCategory=[{"categoryCode":"宝宝奶粉1","categoryName":"111113","categorySort":"3","categorySet":"1","categoryImg":"http://10.19.95.100/uimg/sop/commodity/201312061143447224_x.jpg"},
                {"categoryName":"宝宝奶粉2","categoryCode":"111113","categorySort":"4","categorySet":"1","categoryImg":"http://10.19.95.100/uimg/sop/commodity/201312061143447224_x.jpg"}]



f = a.getResponse()
print(f)
