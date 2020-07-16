#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-3-21

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.CommodityeditCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.advertise='xxx'
a.applyCode='1be9df8f-94fb-43f9-962c-125bfc621a6e'
a.appStoreCode='xx'
a.attrInfo=[{"attrIsMulti":"0(0：否   1：是)","attrName":"温度","attrChoiceInfo":[{"attrChoiceName":"加冰","attrChoiceCode":"xxx"}],"attrCode":"xxx"}]
a.brandCode='xxx'
a.brgew='xx'
a.categoryCode='xx'
a.classifyCode='xxx'
a.cmBarcode='xx'
a.deliveryAttr='01(01－常温 02－恒温 03－冷藏 04－冷冻)'
a.immediateAppoint='01(01：支持  02：不支持)'
a.immediateAppointTime='xxx'
a.operType='00(00：新建 01：审核不通过时修改 02：编辑)'
a.packingPrice='xxx'
a.picUrl='http://xx/xx/xx/xx/x1.jpg(逗号隔开共5张)'
a.productCode='xxx'
a.productName='xxx'
a.purchaseMin='1'
a.qty='xxx'
a.secondClassifyCode='xxx'
a.sellHoursType='01'
a.sellPrice='xxx'
a.sellStatus='1(1：上架   2：下架)'
a.serviceTime='1-24'
a.standardInfo=[{"choiceInfo":[{"choicePrice":"1","choiceCode":"xxx","choiceName":"大杯"}],"isMulti":"0(0：否   1：是)","standardName":"尺寸","standardCode":"xxx"}]
a.storeCode='xxx'
a.supplierCmCode='xxx'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)