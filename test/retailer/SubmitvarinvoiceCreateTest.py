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

a=api.SubmitvarinvoiceCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.appId='111111'
a.snCustNum='111111'
a.submitFlag='submitFlag'
a.vatAddressInfoDTO={"createTime":"createTime","updateTime":"updateTime","street":"street","addrNum":"addrNum","state":"state","postCode":"postCode","city":"city","country":"country","detailAddress":"detailAddress","mobileNumOne":"mobileNumOne","teleExtn":"teleExtn","cntctPointName":"cntctPointName","additionalThree":"additionalThree","addrType":"addrType","teleAreaCode":"teleAreaCode","additionalOne":"additionalOne","teleNum":"teleNum","preferFlag":"preferFlag","mobileNumTwo":"mobileNumTwo","additionalFour":"additionalFour","town":"town","additionalTwo":"additionalTwo","teleCntryCode":"teleCntryCode"}
a.vatInvoiceInfoDTO={"orgAddr":"orgAddr","certType":"certType","bankName":"bankName","orgName":"orgName","vatQlfctStat":"vatQlfctStat","vatQlfctStatUpdRsn":"vatQlfctStatUpdRsn","taxRegCertId":"taxRegCertId","bankDepositAcnt":"bankDepositAcnt","vatConsignId":"vatConsignId","vatQlfctStatUpdTm":"vatQlfctStatUpdTm","certNo":"certNo","taxPayerCertId":"taxPayerCertId","orgTel":"orgTel","bankAcctPermitId":"bankAcctPermitId"}

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)