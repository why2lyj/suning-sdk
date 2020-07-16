#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../../api-sdk-python")
import suning.api as api
'''
Created on 2014年6月6日

@author: dd
'''

a = api.InvaddressAddRequest()
a.streetAddress = '徐庄软件园'
a.invContact = 'test'
a.invName = '测试仓库'
a.invRegion = '00000001'
a.remark = '这是一个测试仓库'
a.invCity = '000001000184'
a.phoneNum = '18051967669'
a.zipCode = '210012'
a.invProvince = '100'
a.telePhone = '18051967669'

try:
    
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)