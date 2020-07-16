#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2016-4-19

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.ProtocolAddRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a226186c2b811ce7fbce83e8a98dc7fe", "435687b33f10f5114a1d2440fe0848c7")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.supplierCode='10000335'
a.supplierBraComp='SEBJ'
a.supplierOffice='1'
a.snCode='5400'
a.supplierApplicationCode='FYBJ14061004'
a.expenseBudgetCode='123456789'
a.areaCopCode='1001'
a.contractDate='2014-05-10'
a.contractCode='12345'
a.adProtocolCity='1'
a.adProtocolRode='1'
a.adProtocolMarket='1'
a.adProtocolBuilding='1'
a.adProtocolArea='200'
a.startDate='2014-05-19'
a.endDate='2014-05-29'
a.paymentLittleMount='30000.00'
a.firstMonthAmount='10000.00'
a.secondPayMonth='5'
a.nextMonthAmount='10000.00'
a.lastPayMonth='11'
a.lastMonthAmount='10000.00'
a.settlementType='1'
a.otherProtocol='1'
a.htmlContent='XHHGHHKJKKKKLGFHJRTIOOJBK...'
a.signNatureContent='XHHGHHKJKKKKLGFHJRTIOOJBK...'
try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)