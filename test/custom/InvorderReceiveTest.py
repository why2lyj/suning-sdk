#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-28

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.InvorderReceiveRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.buySign='1'
a.clientAddress='xx市xx区'
a.clientBank='中国银行'
a.clientBankNum='622848039260099'
a.clientEmail='xxx@163.com'
a.clientName='个人'
a.clientPhone='18551620000'
a.clientTaxNum='622848039260099'
a.clientTel='025-8888'
a.clientType='01'
a.cmmdtys=[{"goodModel":"P","goodGovSign":"0","goodSpecialSign":"不征税","goodCountAmount":"1000","goodDeductions":"-10","goodId":"000101","goodsCode":"600012346","goodTaxAmount":"160","goodTaxCode":"654334","goodDiscount":"5","goodRate":"0.16","goodSerialNum":"0001","goodNum":"10","goodUnit":"台","goodZeroTaxSign":"0","goodContainTaxSign":"1","goodPrice":"100.00","goodsName":"空调"}]
a.countMoney='100'
a.detialSign='0'
a.extendField='xx'
a.howtoPrint='0'
a.oldTicketCode='150003528888'
a.oldTicketNum='62786934'
a.orderNum='32018091901'
a.orderNumPwd='1B0A2C64C2A1A7FAB7DEBE25FED8B742'
a.orderReturnNum='32018091901'
a.orderTime='2018-09-28 14:26:11'
a.payeeName='李四'
a.platformCoding='70069114'
a.receiveMode='02'
a.remark='xx'
a.reviwerName='李五'
a.saleAddress='南京市玄武区苏宁大道1号'
a.saleBank='中国银行'
a.saleBankNum='622848039260099'
a.saleName='南京苏宁软件技术有限公司'
a.saleTaxNum='140301193302051282'
a.saleTel='025-66996699'
a.specialRedSign='0'
a.sysSource='例如：ZY：自营'
a.ticketName='张三'
a.ticketType='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)