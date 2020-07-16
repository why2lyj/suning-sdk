# -*- coding: utf-8 -*-

'''

Created on 2020-3-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoicerecordlistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.invoiceRecordListReqDto = None
        self.queryParam = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryInvoicerecordlist'

    def getApiMethod(self):

        return 'suning.retailer.invoicerecordlist.query'



