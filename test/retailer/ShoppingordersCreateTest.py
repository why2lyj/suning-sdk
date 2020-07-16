#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-8-3

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ShoppingordersCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='af99f27da589fbf089103f2f44c9a'
a.buyerName='张三'
a.buyerPhone='15866728686'
a.createCode='1405648424'
a.discountAmount='0.00'
a.discountCode='6833452575344'
a.installDelivery={"installTownName":"江宁","installProvinceCode":"320000","installTownCode":"320112","installDistrictName":"江宁区","installDistrictCode":"320112","installCityCode":"320100","installProvinceName":"江苏省","installPhone":"18632678623","installBuyerAddress":"XXX路31号XXX大厦A座2楼","installCityName":"南京市","installName":"张三"}
a.merchantCustNo='1701014245'
a.orderAmount='2862.00'
a.orderDelivery={"districtName":"江宁区","districtCode":"320112","townName":"江宁","provinceCode":"320000","cityName":"南京市","cityCode":"320100","receiverName":"张三","provinceName":"江苏省","buyerAddress":"XXX路31号XXX大厦A座2楼","townCode":"320112","receiverPhone":"18632486868"}
a.orderFrom='1'
a.orderItem=[{"cmmdtyCode":"E232A1000000157","sellPrice":"2800.00","supplierName":"苏宁","shipMethod":"1","orderType":"1","unitPrice":"27800.00","supplierCode":"SN","distributorCode":"0000000000","installFlag":"0","cmmdtyName":"空调","hopeArrivalTime":"2018-07-01","serviceCode":"556421389","quantity":"1","bookTimeDetail":"2018-07-01","totalPayAmount":"2800.00","outerOrderItemNo":"1004654"}]
a.outerOrderNo='4343424'
a.payAmount='2862.00'
a.posCode='6849451548'
a.remark='备注信息'
a.salesMode='1'
a.storeCode='1232130002'
a.userCode='00000012313'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)