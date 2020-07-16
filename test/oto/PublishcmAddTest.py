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

a=api.PublishcmAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.assortCode='11111111'
a.childItem=[{"supplierImg1Url":"1","price":"11","productCode":"104007723","itemCode":"561"}]
a.cmTitle='11'
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"1","moduleName":"1","type":"cat_mod"}]
a.introduction='商家商品介绍'
a.itemCode='789123'
a.mainPicVideoCode='108625'
a.packingList=[{"packingListQty":"1","packingListName":"\t电脑"}]
a.price='5.00'
a.productCode='102652866'
a.saleDate='2016-09-30'
a.saleSet='1'
a.sellPoint='卖点'
a.supplierImg1Url='1'
a.supplierImg2Url='1'
a.supplierImg3Url='1'
a.supplierImg4Url='1'
a.supplierImg5Url='1'
a.targetChannel='1'
a.videoCode='108625'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)