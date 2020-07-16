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

a=api.CmmdtyinfoModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.activityPic='http://1.jpg'
a.afterSaleServiceDec='324234'
a.childItem=[{"supplierImgAUrlX":"http://1.jpg","productCodeX":"100000001","itemCodeX":"1"}]
a.cmTitle='4324'
a.detailModule=[{"content":"34","num":"1","moduleId":"R2701001_1","moduleName":"优惠信息","type":"cat_mod"}]
a.introduction='23123'
a.itemCode='324234'
a.ltpic='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.mainPicVideoCode='108625'
a.packingList=[{"packingListQty":"1","packingListName":"电脑"}]
a.productCode='4324'
a.sellPoint='34234'
a.supplierImgAUrl='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImgBUrl='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImgCUrl='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImgDUrl='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.supplierImgEUrl=' 	http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.videoCode='108625'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)