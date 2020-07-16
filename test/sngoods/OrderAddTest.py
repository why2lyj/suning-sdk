#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-2-25

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.address='江苏省南京市雨花区软件大道舜天集团'
a.amount='100.00'
a.channelcode='1'
a.cityId='010'
a.countyId='17'
a.hopeArrivalTime='2019-11-06-3'
a.invoiceState='是否开发票：1=开；0=不开'
a.invoiceTitle='发票抬头（发票类型为2电子发票时必传）'
a.invoiceType='发票类型：1-增值税专票；；2-电子发票 ，（invoiceState是否开票=1时必填）'
a.mobile='15311351111'
a.payment='支付方式：01-在线支付-易付宝； 02-企业汇款支付； 03-代扣支付'
a.provinceId='010'
a.receiverName='张三'
a.remark='备注（不多于80个汉字）'
a.servFee='5.00'
a.sku=[{"num":"10","skuId":"123456789","unitPrice":"10.00","supplierCode":"0000000000"}]
a.specialVatTicket={"taxNo":"纳税人识别号：数字或字母，字段长度为15、18、20位 ","consigneeName":"收票件人姓名（发票类型为1增值税专票必传）","regTel":"18767890345","consigneeAddress":"收票件人地址（发票类型为1增值税专票必传）","regAdd":"江苏省南京市雨花区软件大道舜天集团","regAccount":"23235254664336","regBank":"453453434534354","consigneeMobileNum":"收票件人电话（发票类型为1增值税专票必传）"}
a.telephone='010-84728989'
a.townId='03'
a.tradeNo='123456789'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)