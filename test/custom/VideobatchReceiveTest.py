#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-9-4

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.VideobatchReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.source='ISV'
a.type='A'
a.videoList=[{"duration":"1000","widthHeight":"1280*720","videoSizeKb":"1000","videoCode":"30614447","videoUrlId":"0a2dnq-XpqSjmamL4K2doafho6CimqqZpw","videoId":"159264703","videoName":"火影忍者疾风传","videoUrlTv":"PP返回的pptvsPlayStr字段","videoSize":"100","classifyName":"云台助手"}]
a.videoType='2'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)