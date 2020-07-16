# -*- coding: utf-8 -*-
'''
Created on 2014-5-21
@author: momo
<br>
测试类
'''
import sys
sys.path.append("../../../api-sdk-python")
import suning.api


a = suning.api.ParallelinvareaSetRequest()

a.invProvinces = {"invProvince": [{"invProvinceCode": "230"}, {"invProvinceCode": "240"}]}
a.invCitys = {"invCity": [{"invCityCode": "111"}, {"invCityCode": "222"}]}
a.invCode = 's1234'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)
    

    
    
    
    
    
    
    
    
    
    
    