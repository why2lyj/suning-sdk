#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-8-22

@author: suning
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.ShopInfoModifyRequest()
a.placard = "心心相印"
a.telphone = "010-11255555"

f = a.getResponse()
print(f)
