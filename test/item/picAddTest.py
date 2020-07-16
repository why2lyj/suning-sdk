# -*- coding: utf-8 -*-
"""
Created on 2014-5-21
@author: momo
<br>
测试类
"""
import sys
sys.path.append("../../../api-sdk-python")

import suning.api


a=suning.api.PicAddRequest()
a.setFilePath('140526NBCX66415786.jpg')

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)