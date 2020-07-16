#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-3-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CulitemcontentreviseModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.afterSaleServiceDec='七天包退换'
a.assortCode='11111111'
a.cmTitle='商品标题'
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"123","moduleName":"模块名称","type":"cat_mod"}]
a.freightTemplateId='9787511002884'
a.highlightWordone='亮点词1'
a.highlightWordthree='亮点词3'
a.highlightWordtwo='亮点词2'
a.introduction='单一详情'
a.itemCode='111'
a.mainPicVideoCode='主图视频编码'
a.productCode='105560068'
a.salesDate='2014-01-06'
a.saleSet='0'
a.sellPoint='十万个为什么'
a.supplierImgAUrl='商家商品图片1地址url'
a.supplierImgBUrl='商家商品图片2地址url'
a.supplierImgCUrl='商家商品图片3地址url'
a.supplierImgDUrl='商家商品图片4地址url'
a.supplierImgEUrl='商家商品图片5地址url'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)