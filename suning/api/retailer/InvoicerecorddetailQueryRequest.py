# -*- coding: utf-8 -*-

'''

Created on 2020-3-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoicerecorddetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.omsOrderItemNo = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryInvoicerecorddetail'

    def getApiMethod(self):

        return 'suning.retailer.invoicerecorddetail.query'



