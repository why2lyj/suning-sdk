#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-10-23

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderinfoReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cfOrderId='123456789'
a.orderDate='2013-06-28'
a.orderTime='15:00:00'
a.orderSource='B2C'
a.salePlatform='DJ'
a.orderChannel='PC'
a.orderMemo='需要送货'
a.orderItemQty='99'
a.cfTradePays=[{"parentPaymentCode":"50","totalPayAmount":"10.00","paymentCode":"5002"}]
a.payItemQty='99'
a.orderSaleTotalAmt='12000'
a.realPayAmt='12000'
a.totalSrvFee='12000'
a.totalTax='12'
a.totalShippingFee='12000'
a.orderSerialNumber='1'
a.cfOrders=[{"cmmdtyCode":"101002405","itemTaxFare":"12.12","srvFee":"12000","cfLogistics":{"hopeArrivalDate":"2012-05-23","verifyCode":"5123","hopeArrivalTime":"15:00:00"},"basicFee":"12000","weight":"12.12","pointMoney":"12.00","continuousFee":"12000","transportFee":"12000","cfOrderPays":[{"payAmount":"1234.00","payCode":"5002","payName":"电子礼金券","payDate":"2012-05-23","payTime":"15:00:00","parentPayCode":"50"}],"cmmdtyName":"sony彩电","cfOrderItemId":"12345678901","price":"12000","couponTotalMoney":"12000","pointAmount":"12000","voucherTotalMoney":"500.00","saleQty":"12000","totalAmount":"12000","managerCardMoney":"12000","storeCode":"8884","cfTransactions":[{"mobPhoneNum":"13588888888","deliveryAddrMain":"南京市白下区淮宁电器大厦18F","consignee":"孙一二","longitude":"1","latitude":"1"}]}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)