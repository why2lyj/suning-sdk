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

a=api.ItemAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityPic='http://1.jpg'
a.barpic='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.brandCode='A101'
a.categoryCode='R6101011'
a.childItem=[{"barpicX":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","supplierImgAUrl":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","parsX":[{"parValueX":"红色","parCodeX":"G00001"}],"barcode":"11","priceX":"1.11","itemCodeX":"子商品商家商品编码"}]
a.cmTitle='商品标题'
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"R2701001_1","moduleName":"优惠信息","type":"cat_mod"}]
a.introduction='电脑详情'
a.itemCode='商家商品编码'
a.ltpic='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.mainPicVideoCode='108625'
a.packingList=[{"packingListQty":"1","packingListName":"电脑"}]
a.pars=[{"parCode":"cm_model","parValue":"1"}]
a.price='100.11'
a.productName='商品名称'
a.sellPoint='卖点'
a.supplierImg1Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg2Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg3Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg4Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImg5Url='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.videoCode='108625'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)