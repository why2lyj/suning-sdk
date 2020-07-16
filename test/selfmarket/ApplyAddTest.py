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

a=api.ApplyAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.barpic='http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg'
a.brandCode='A101'
a.categoryCode='R6101011'
a.childItem=[{"barpicX":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","supplierImgAUrl":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","parsX":[{"parValueX":"红色","parCodeX":"111"}],"barcode":"11","itemCodeX":"111"}]
a.cmTitle='商品标题'
a.conventionBeginTime='2018-02-13 11:37:00'
a.conventionEndTime='2018-02-13 11:37:00'
a.conventionPoints='常规促销卖点'
a.detailModule=[{"content":"模块化详情内容","num":"1","moduleId":"123","moduleName":"模块名称","type":"cat_mod"}]
a.endTime='2018-02-13 11:37:00'
a.highBeginTime='2018-02-13 11:37:00'
a.highEndTime='2018-02-13 11:37:00'
a.highlightWordone='亮点词1'
a.highlightWordthree='亮点词3'
a.highlightWordtwo='亮点词2'
a.highPoints='高级促销卖点'
a.introduction='好品质好商品'
a.itemCode='naikeabc'
a.mainPicVideoCode='108625'
a.mobilePromotionLink='http://shop.suning.com/70088824/10108744.html'
a.packingList=[{"packingListQty":"1","packingListName":"电脑"}]
a.pars=[{"parCode":"cm_model","parValue":"1"}]
a.productName='大衣'
a.promotionFlag='是'
a.promotionLink='http://shop.suning.com/70088824/10108744.html'
a.promotionPoints='活动关联文案'
a.sellingPoints='商品卖点'
a.startTime='2018-02-13 11:37:00'
a.supplierImgUrl=[{"urlE":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","urlD":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","urlC":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","urlB":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg","urlA":"http://10.19.95.100/uimg/sop/commodity/181223352817344502976922_x.jpg"}]
a.videoCode='108625'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)