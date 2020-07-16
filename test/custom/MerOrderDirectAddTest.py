#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2017-12-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.MerOrderDirectAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.cityCode='025'
a.cmmdtyQaType='0'
a.consignee='张三'
a.extdCmmdtyBand='0000137D5'
a.extdCmmdtyCtgry='R0125658'
a.extdCommodityCode='42346869'
a.extdCommodityName='挂壁式空调'
a.faultTypeCode='B1202004'
a.mobPhoneNum='18551600409'
a.orderChannel='ZL'
a.orderTime='20160414175115'
a.phoneNum='073586131462'
a.proName='02'
a.saleDate='20130222162020'
a.saleQty='5'
a.salesPerson='75324568'
a.sapOrderType='ZS01'
a.serviceTime='20160420093018'
a.sourceOrderItemId='752316542542535'
a.srvAddress='随机数字；小区/大厦/单位/村；市；区/县/开发区；镇/街道办；路/道/街；巷/弄；号；详细地址'
a.srvAreaCode='0250199'
a.srvMemo='需要带支架，需要维修'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)