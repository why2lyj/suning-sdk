#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-4-15

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CulitemAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.afterSaleServiceDec='七天内包退换'
a.alertQty='10'
a.assortCode='11111'
a.auditFlag='X'
a.brandCode='000C'
a.categoryCode='R00001'
a.cmTitle='111'
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"123","moduleName":"模块名称","type":"cat_mod"}]
a.introduction='111'
a.invQty='100'
a.itemCode='12233'
a.pars=[{"parCode":"111","parValue":"111"}]
a.peopleNum='2'
a.pingouPrice='20.00'
a.price='20.00'
a.productName='平凡的世界'
a.purchaseMin='5'
a.saleCatalogCode='262676'
a.saleDate='2014-01-06'
a.saleSet='0'
a.sellPoint='好品质'
a.supplierImgAUrl='11'
a.supplierImgBUrl='11'
a.supplierImgCUrl='11'
a.supplierImgDUrl='111'
a.supplierImgEUrl='111'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)