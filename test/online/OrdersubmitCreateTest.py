#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-11-29

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
a.platFormTrade={"taxPayerAddr":"南京市白下区淮宁电器大厦18F","invoiceTitleType":"01","bankAccntNum":"6YUIOP3456789009876","activityNum":"201909090001","chanId":"01","cartTwoNo":"DLJA2018114812000000","taxPayerNo":"21111","receiverStreet":"淳化街道","receiverAddress":"修文路9号","invoiceTitle":"个人消费","totalNo":"2","receiverName":"张三","installmentNum":"6","taxPayerName":"张三","orderId":"123342312","receiverPhone":"025-22222222","bespoke":"Y","memberNo":"23456543","platFormOrder":[{"orderItemId":"22222222222222","fullReductionInfo":[{"fullReductionAmount":"2.00","fullReductionType":"1","bonusId":"2079097","promotionNum":"1233434","provider":"01"}],"businessSign":"0","selectedInstallDate":"123","saleNum":"3","snSkuId":"123456789","postage":"5.00","activityId":"201419801004**","orderPayment":"10.00","totalFee":"12.00","price":"100.00","pointAmount":"1.00","giftCardList":[{"giftCardAmount":"10.00","giftCardCode":"1232332342","giftCardType":"01"}],"orderItemStatus":"01","skuId":"1234","selectedArrivalTime":"2018-08-01-2","couponInfo":[{"couponAmount":"1.00","couponType":"01","couponCode":"21212"}]}],"payment":"100.00","orderType":"A001","regPhone":"02584418888","isSupportPromotion":"0","receiverCounty":"江宁区","invoiceType":"01","receiverMobile":"12345678900","receiverProvince":"江苏省","accntBank":"南京银行","regAddr":"举例：南京市白下区淮海路68号苏18F","receiverNationality":"中国","orderStatus":"01","taxMobilePhone":"02584418888","receiverCity":"南京市","taxPayerPhone":"02584418888","receiverZip":"210000","invoiceContent":"餐饮"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)