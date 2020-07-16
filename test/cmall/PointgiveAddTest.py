#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-7-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PointgiveAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.custNum='6143457056'
a.deviceId='aafadfadf'
a.ecoType='140000000010'
a.invokerCode='pptv'
a.order={"store":"8371","cmdtyName":"aada","orderItemId":"A101602061818477844","orderType":"DXHDT","addAmt":"11","cmdtyCode":"adadd","supplierCode":"如果积分发放主体类型为209000000020时，此字段必填","supplierType":"209000000020","cmdtyBrand":"adad","cmdtyCatalog":"aad","accountType":"8012","branch":"5006","cmdtyGroup":"adaa","orderAmt":"10","orderTypeDesc":"aaa"}
a.orderId='aaaaaa'
a.sceneCode='场景编码'
a.sceneType='PE1110'
a.transId='d7bb1090e11c4ab398b38ab75efa6e02'
a.transTimestamp='2016-05-06 18:18:47:691'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)