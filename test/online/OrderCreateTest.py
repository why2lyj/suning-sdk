#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-9-4

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.platFormTrade={"taxPayerAddr":"南京市白下区淮宁电器大厦18F","invoiceTitleType":"01","bankAccntNum":"6YUIOP3456789009876","chanId":"01","cartTwoNo":"DLJA2018114812000000","taxPayerNo":"21111","receiverStreet":"淳化街道","receiverAddress":"修文路9号","invoiceTitle":"个人消费","totalNo":"2","receiverName":"张三","taxPayerName":"张三","orderId":"123342312","memberNo":"23456543","bespoke":"Y","receiverPhone":"025-22222222","platFormOrder":[{"orderItemId":"22222222222222","fullReductionInfo":[{"fullReductionAmount":"2.00","activityId":"1233434","fullReductionType":"1","bonusId":"2079097","provider":"01"}],"businessSign":"0","selectedInstallDate":"123","saleNum":"3","postage":"5.00","orderPayment":"10.00","totalFee":"12.00","price":"100.00","pointAmount":"1.00","giftCardList":[{"giftCardAmount":"10.00","giftCardCode":"1232332342","giftCardType":"01"}],"orderItemStatus":"01","outerSkuId":"123456789","skuId":"1234","promotionNum":"201419801004**","selectedArrivalTime":"2018-08-01-2","couponInfo":[{"couponAmount":"1.00","couponType":"01","couponCode":"21212"}]}],"payment":"100.00","orderType":"A001","regPhone":"02584418888","isSupportPromotion":"0","receiverCounty":"江宁区","invoiceType":"01","receiverMobile":"12345678900","accntBank":"南京银行","receiverProvince":"江苏省","regAddr":"举例：南京市白下区淮海路68号苏18F","receiverNationality":"中国","orderStatus":"01","taxMobilePhone":"02584418888","receiverCity":"南京市","taxPayerPhone":"02584418888","receiverZip":"210000","invoiceContent":"餐饮"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)