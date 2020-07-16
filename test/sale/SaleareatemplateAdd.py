#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api
'''
Created on 2014年6月5日

@author: dd
'''

a = api.SaleareatemplateAddRequest()
a.nation = '0'
a.provList = {"prov": ["260","070"]}
a.cityList = {"city": ["000001000197","000001000198"]}
a.templateName = u'新增省份和城市'

try:
    
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)