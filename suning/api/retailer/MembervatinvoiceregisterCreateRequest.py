# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class MembervatinvoiceregisterCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.merchantCustNo = None
        self.regAddr = None
        self.regBankAccount = None
        self.regBankName = None
        self.regCompanyName = None
        self.regPhone = None
        self.submitFlag = None
        self.taxationRegNo = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'regAddr':{'allow_empty':False},
        	'regBankAccount':{'allow_empty':False},
        	'regBankName':{'allow_empty':False},
        	'regCompanyName':{'allow_empty':False},
        	'regPhone':{'allow_empty':False},
        	'submitFlag':{'allow_empty':False},
        	'taxationRegNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createMembervatinvoiceregister'

    def getApiMethod(self):

        return 'suning.retailer.membervatinvoiceregister.create'



