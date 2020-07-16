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

a=api.InitmerchantstoreCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='111111'
a.coperator='操作人'
a.dyttInitMerchantInfoDTO={"idcardFrontUrl":"http://11.jpg","provName":"江苏省","acctNo":"086631","companyAddr":"苏宁大道1号","townName":"全区","cityName":"南京市","registPhone":"254544","cityCode":"025","generalTaxpayerFlag":"0","snCustNum":"7017963441","companyName":"苏宁","legalPerson":"法人姓名","townCode":"99","openingBankAccount":"6254540546545450","districtName":"玄武区","licenseNo":"0265454651544x4","districtCode":"01","idcardReverseUrl":"http://22.jpg","openingBankName":"中国银行","companyType":"1","legalIdcardNo":"3201225546548844","provCode":"100","licenseUrl":"http://11.jpg"}
a.dyttInitSotreInfoDTO={"storeTownCode":"99","contractStartDate":"2020-02-23","storeCityName":"南京市","storeYtCode":"门店业态","storeProvCode":"100","zipCode":"0250000","snStoreCode":"90N3","startBusinessDate":"2020-03-23","regionCode":"10001","contactPhone":"16546545","storeName":"店铺名称","areaCode":"025","storeXzCode":"1","businessType":"1","storeLvCode":"1","storeSource":"4","storeTownName":"全区","detailAddress":"苏宁大道1号","companyCode":"5016","responsiblePerson":"筹建负责人","storeProvName":"江苏省","storeDistrictName":"玄武区","storeCityCode":"025","storeType":"ST5","isManage":"Y","contactPerson":"张三","storeCode":"59021","storeDistrictCode":"01","responsiblePhone":"1654561544121"}
a.operType='0'
a.platformCode='P6'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)