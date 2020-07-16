#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-7-8

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.freightTemplateAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.commonMap={"shippingType":"0","firstItemFare":"10.01","firstBulkFare":"10.01","firstWeightFare":"3.01","freightTemplateName":"模版名称","continuedBulkFare":"2.01","continuedItemFare":"3.01","firstItem":"10","continuedtBulk":"2.01","supplierType":"H","continuedWeight":"5.01","continuedItem":"5","firstWeight":"10.01","valuationType":"0","taxType":"0","firstBulk":"3.01","continuedWeightFare":"2.01"}
a.specialList=[{"speFirstItemFare":"10.02","speContinuedItemFare":"2.03","speFirstItem":"5","speContinuedItem":"10","speFirstBulkFare":"5.02","speProvenCode":"140,150,160","speContinuedWeight":"3.03","speContinuedWeightFare":"2.05","speFirstWeightFare":"10.01","speContinuedtBulkFare":"5.01","speCityEnCode":"000001000174,000001000175,000001000176","speFirstWeight":"5.07","speFirstBulk":"10.08","speRenCode":"243","speContinuedtBulk":"5.02"}]
a.vendorCode='0070057239'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)