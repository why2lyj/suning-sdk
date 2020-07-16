# -*- coding: utf-8 -*-

'''

Created on 2020-3-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoicedetailitemlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.invoiceType = None
        self.omsOrderNos = None
        self.snCustNum = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryInvoicedetailitemlist'

    def getApiMethod(self):

        return 'suning.retailer.invoicedetailitemlist.query'



