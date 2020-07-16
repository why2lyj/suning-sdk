#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月3日

@author: dd
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a=api.LogisticcompanyGetRequest()
a.companyName='D速快递'


f = a.getResponse()
print(f)
