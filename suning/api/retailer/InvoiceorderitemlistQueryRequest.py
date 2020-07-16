# -*- coding: utf-8 -*-

'''

Created on 2020-3-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoiceorderitemlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.invoiceOrderItemQueryReqDto = None
        self.queryParam = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryInvoiceorderitemlist'

    def getApiMethod(self):

        return 'suning.retailer.invoiceorderitemlist.query'



