#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-5-18

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PublishcmAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.productCode='102652866'
a.sellPoint='卖点'
a.cmTitle='商品标题'
a.price='123'
a.itemCode='主商品商家商品编码。'
a.introduction='商家商品介绍'
a.packingList=[{"packingListQty":"1","packingListName":"装箱清单名单"}]
a.childItem=[{"supplierImgAUrl":"http://1.jpg","priceX":"11","productCodeX":"104007723","itemCodeX":"561"}]
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"R6151002_1","moduleName":"模块名称","type":"cat_mod"}]
a.supplierImgUrlA='http://1.jpg'
a.supplierImgUrlB='http://1.jpg'
a.supplierImgUrlC='http://1.jpg'
a.supplierImgUrlD='http://1.jpg'
a.supplierImgUrlE='http://1.jpg'
a.ltpic='http://1.jpg'
a.afterSaleServiceDec='22'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)