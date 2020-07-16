#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-9-29

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CommoditybatchesAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.commodityBatches=[{"supCommodityCode":"20190719140000000","manufacturer":"上海东海制药股份有限公司","expiryDate":"20190910","operationTime":"20190910152633001","batchesCode":"20190910","supplierCode":"10000197","commodityName":"速效救心丸","storeCode":"9WF4","specifications":"规格:10粒*6板/盒","commodityCode":"1000001002","deleteType":"D-删除，其他为空"}]

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)