# -*- coding: utf-8 -*-

'''

Created on 2020-3-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class SubmitvarinvoiceCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.snCustNum = None
        self.submitFlag = None
        self.vatAddressInfoDTO = None
        self.vatInvoiceInfoDTO = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createSubmitvarinvoice'

    def getApiMethod(self):

        return 'suning.retailer.submitvarinvoice.create'



