#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-5-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.VedioModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.classifyName='云台助手'
a.source='MSOP'
a.type='A'
a.videoCode='30614447'
a.videoId='159264703'
a.videoName='火影忍者疾风传'
a.videoSize='100'
a.videoSizeKb='1000'
a.videoUrlId='0a2dnq-XpqSjmamL4K2doafho6CimqqZpw'
a.videoUrlTv='PP返回的pptvsPlayStr字段'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)