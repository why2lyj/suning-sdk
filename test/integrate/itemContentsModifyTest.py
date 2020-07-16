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

a=api.itemContentsModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.afterSaleServiceDec='一年内包退换'
a.assortCode='11111111'
a.childItem=[{"supplierImg1Url":"http://1.jpg...","productCode":"11000000002","itemCode":"11"}]
a.cmTitle='商品标题'
a.detailModule=[{"content":"5aW95ZWG5ZOB","num":"1","moduleId":"1","moduleName":"售后服务","type":"usr_mod"}]
a.introduction='5aW95ZWG5ZOB'
a.itemCode='naikeabc'
a.mobile={"summary":"1","listInfo":[{"text":"1","num":"1","pic":"http://1.jpg"}]}
a.mobileNew={"module":[{"imgUrl":"http://1.jpg","moduleName":"售后服务","moduleStatus":"0","tuijianId":"1","couponId":"1"}]}
a.packingList=[{"packingListQty":"1","packingListName":"装箱清单名称"}]
a.peopleNum='5'
a.productCode='1000000001'
a.purchaseMin='5'
a.saleDate='2013-10-1'
a.saleSet='0'
a.sellPoint='好东西'
a.sourceCountry='11111111'
a.supplierImg10Url='http://1.jpg...'
a.supplierImg1Url='http://1.jpg...'
a.supplierImg2Url='http://1.jpg...'
a.supplierImg3Url='http://1.jpg...'
a.supplierImg4Url='http://1.jpg...'
a.supplierImg5Url='http://1.jpg...'
a.supplierImg6Url='http://1.jpg...'
a.supplierImg7Url='http://1.jpg...'
a.supplierImg8Url='http://1.jpg...'
a.supplierImg9Url='http://1.jpg...'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)