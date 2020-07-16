#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-3-27

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.InvoicerecordlistQueryRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='appId'
a.invoiceRecordListReqDto={"cmmdtyCode":"1","startDate":"1","platformCode":"P2","btcOrderId":"1","submitTypeInvoice":"1","invoiceType":"1","startCreateOrderTime":"1","endDate":"11","omsOrderItemId":"1","merchantCustNo":"11","creator":"1","linkerMobile":"1","cmmdtyName":"1","endCreateOrderTime":"1","omsOrderId":"11","orderId":"1"}
a.queryParam={"psize":"1","pnumber":"1","corderBy":"1"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)