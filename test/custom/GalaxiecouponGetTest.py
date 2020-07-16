#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-16

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.GalaxiecouponGetRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityId='202004010001299290'
a.activitySecretKey='fXO2jW434G9EXtTUelN71K5U'
a.appVersion='8.7.2.3'
a.bonusTrigerId='3'
a.cityId='2'
a.detect='mmds_97fc62e6ea2c41abf7745f51622c67b3'
a.dfpToken='THc0gl1713dc37bc5gJJx2a58'
a.idfToken='THE0Kg17157544d8fsIFbb0d0___w7DDp8KLw75ow5MZbMOyImjCqsONBcOFw7hawqrCssOg'
a.memberId='1234567890'
a.miniSource='wechat'
a.requestIp='10.96.193.66'
a.serialNo='snyg612_39eaf0e06bbc54c387425bd94990f80c'
a.snUnionId='bfb3ae009a31e98f4fa13ee41c6cbfb3ae01f9a31e9884fa'
a.terminalId='32'
a.termiSys='Windows'
a.valiNo='202004010001299291+6002318564'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)