#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月3日

@author: dd
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../"
sys.path.append(basepath)

import suning.api as api

a=api.LogisticcompanyQueryRequest()


## 不使用config.py中定义的appkey 和 appsecret 的话就直接调用下面这个方法
a.setDomainInfo("openpre.cnsuning.com","80")

# 如果个别接口有需要单独使用appkey 和 appsecret的需求 就调用以下方法
a.setAppInfo("a494d8bb97a0d34e3e2f4caf7fa30dd8", "fcf825f1e8d605e84f4a3064fc171c2b")

# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
 
a.pageSize = "10"
a.pageNo= "1"

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)
