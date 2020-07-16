#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018-7-18

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ApplicationPrivilegeCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.applyHead={"areaCompanyCode":"5400","startDate":"2018-05-01","settlementType":"1","supplierApplicationCode":"HDIC180622578","supplierCode":"10000335","endDate":"2018-05-20","expenseBudgetCode":"HDC0001566","applyLevel":"FGS","htmlContent":"HTML ENCODE:UTF-8","productBrand":"1659","actionDescribe":"五一门店促销活动","snCode":"5400","payType":"3","payDate":"2018-06-04","invoiceContent":"3"}
a.areaDetail=[{"operateAreaCompany":"1020","operateAreaShoper":"4687"}]
a.itemDetail=[{"wareHouse":"0001","chargeItem":"不限","favoureAmount":"100.2","channel":"99","comments":"商品优惠","itemCode":"101092731"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)