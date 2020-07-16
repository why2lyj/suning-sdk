#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2020-5-18

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.InvoiceConfirmRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyForInvoiceReqDTO={"markId":"xxx1000000","consigneeName":"张三","regTel":"18767890345","remark":"100006759913","regAdd":"江苏省南京市雨花区软件大道舜天集团","invoiceType":"6","companyName":"江苏舜天有限公司","consigneeMobileNum":"17856789012","taxNo":"32534346637","title":"南京苏宁软件有限公司","address":"江苏省南京市秦淮区法院","regAccount":"23235254664336","invoiceContent":"22","regBank":"453453434534354"}
a.orderInfoDTO=[{"gcOrderNo":"23423524334"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)