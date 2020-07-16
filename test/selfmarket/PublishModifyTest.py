#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-11-16

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.PublishModifyRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cmTitle='商品标题'
a.conventionBeginTime='2018-02-13 11:37:00'
a.conventionEndTime='2018-02-13 11:37:00'
a.conventionPoints='常规促销卖点'
a.detailModule=[{"content":"5qih5Z2X5YyW6K+m5oOF5YaF5a65","num":"1","moduleId":"R2701001_1","moduleName":"优惠信息","type":"usr_mod"}]
a.endTime='2018-02-13 11:37:00'
a.highBeginTime='2018-02-13 11:37:00'
a.highEndTime='2018-02-13 11:37:00'
a.highPoints='高级促销卖点'
a.introduction='电脑详情'
a.itemCode='naikeabc'
a.mobilePromotionLink='http://shop.suning.com/70088824/10108744.html'
a.packingList=[{"packingListQty":"1","packingListName":"电脑"}]
a.productCode='750047486'
a.promotionFlag='是'
a.promotionLink='http://shop.suning.com/70088824/10108744.html'
a.promotionPoints='活动关联文案'
a.sellingPoints='商品卖点'
a.startTime='2018-02-13 11:37:00'
a.supplierImgUrl=[{"urlE":"http://10.19.95.100/uimg/sop/commodity/623952902322391517989000_x.jpg","urlD":"http://10.19.95.100/uimg/sop/commodity/623952902322391517989000_x.jpg","urlC":"http://10.19.95.100/uimg/sop/commodity/623952902322391517989000_x.jpg","urlB":"http://10.19.95.100/uimg/sop/commodity/623952902322391517989000_x.jpg","urlA":"http://10.19.95.100/uimg/sop/commodity/623952902322391517989000_x.jpg"}]
a.videoCode='108625'
a.mainPicVideoCode='108991'
a.highlightWordone='亮点词1'
a.highlightWordtwo='亮点词2'
a.highlightWordthree='亮点词3'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)