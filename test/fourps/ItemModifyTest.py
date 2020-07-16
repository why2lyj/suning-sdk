#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-8-15

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ItemModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.supplierCmCode='1'
a.productName='1'
a.gbCode='1'
a.cmLength='1'
a.cmWidth='1'
a.cmHeight='1'
a.cmVolume='1'
a.grossWeight='1'
a.netWeight='1'
a.shelfLifeFlag='1'
a.packingList='1'
a.shelfLife='1'
a.categoryName1='1'
a.categoryName2='1'
a.brandName='1'
a.standard='1'
a.model='1'
a.categoryCode='1'
a.brandCode='1'
a.cmType='1'
a.cmTitle='1'
a.cmArea='1'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)