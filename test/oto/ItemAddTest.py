#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-11-17

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ItemAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.categoryCode='R6101011'
a.brandCode='A101'
a.productName='电脑'
a.sellPoint='卖点'
a.saleSet='1'
a.cmTitle='标题'
a.targetChannel='1'
a.price='100.11'
a.itemCode='111'
a.assortCode='210002118'
a.transparent='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg1Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg2Url='>http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg3Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg4Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg5Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.pars=[{"parCode":"LAENG","parValue":"1"}]
a.childItem=[{"barpic":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","supplierImg1Url":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","price":"1.11","barcode":"11","pars":[{"parCode":"LAENG","parValue":"1"}],"itemCode":"111"}]
a.barpic='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.introduction='电脑详情'
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"R2701001_1","moduleName":"优惠信息","type":"cat_mod"}]
a.packingList=[{"packingListQty":"1","packingListName":"电脑"}]
a.saleDate='2016-10-11'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)