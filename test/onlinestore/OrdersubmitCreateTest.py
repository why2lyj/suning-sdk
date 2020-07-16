#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-3-11

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrdersubmitCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.platFormTrade={"taxPayerAddr":"南京市白下区淮宁电器大厦18F","invoiceTitleType":"02","bankAccntNum":"6YUIOP3456789009876","cityName":"北京市","chanId":"02","cartTwoNo":"DLJA2018114812000000","taxPayerNo":"SDFDFD458976","receiverAddress":"南京市","invoiceTitle":"个人消费","receiverName":"张三","taxPayerName":"张三","orderId":"123342312","mapType":"01","memberNo":"23456543","platFormOrder":[{"orderItemId":"242342423","fullReductionInfo":[{"fullReductionAmount":"20.00","bonusId":"324425345","promotionNum":"43242","provider":"02"}],"saleNum":"10","snSkuId":"3244234234","postage":"0.00","activityId":"67678678787","orderPayment":"32.00","cartTwoItemNo":"4324242343","totalFee":"23.00","price":"10.00","pointAmount":"3.00","cmmdtyProperty":"01","skuId":"4244242","hopeArrivalTime":"2020-02-14 00:00:00","couponInfo":[{"couponAmount":"2.00","couponType":"02","couponCode":"3221233"}]}],"payment":"100.00","poiId":"234243","deliveryType":"02","regPhone":"02584418888","invoiceType":"05","receiverMobile":"15008987656","accntBank":"南京银行","regAddr":"南京市白下区淮海路68号苏18F","orderTime":"2020-02-14 00:00:00","businessSign":"1","shopCode":"001","taxMobilePhone":"15509876789","taxPayerPhone":"02584418888","shopName":"小店","invoiceContent":"餐饮"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)