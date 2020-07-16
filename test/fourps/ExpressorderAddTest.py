#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-3-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ExpressorderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.expressCompCode='SN2'
a.marketingProduct='10'
a.orderSource='201'
a.packageList=[{"selfFeedingPoint":"L025","serviceMode":"01","packageNo":"1","packageName":"手机","signReturn":"1","pickupMode":"01","agentAmount":"1253.33","carFlag":"0","specialCarType":"空","insyredValue":"15000","packageWeight":"3","fullCarType":"T180","packageLength":"22","outOrderNum":"25845632555555","goodsQty":"3","expressNo":"6258986525522","packageHeight":"64","packing":"1","packageVolume":"3333333","packageWidth":"64","transportType":"01","dstributeAndInstall":"0","packageComment":"备注","agentOption":"02"}]
a.receiverAddressDetail='仙女路'
a.receiverCity='扬州市'
a.receiverCompany='苏宁易购'
a.receiverDistrict='江都区'
a.receiverMobile='13802520698'
a.receiverName='李四'
a.receiverProvince='江苏省'
a.receiverTel='025-66996699'
a.receiverTown='全区'
a.senderAddressDetail='文苑路南京财经大学'
a.senderCity='南京市'
a.senderCompany='苏宁云商有限公司'
a.senderDistrict='栖霞区'
a.senderMobile='13802356421'
a.senderName='张山'
a.senderProvince='江苏省'
a.senderTel='025-66996699'
a.senderTown='全区'
a.uuid='2564EDSF1287RFDROPIG4567IUYT2594IJHG'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)