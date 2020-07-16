# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoiceCheckResultQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.snCode = None
        self.startDate = None
        self.endDate = None
        self.invoiceNum = None
        self.invoiceCode = None
        self.invoiceModel = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryInvoiceCheckResult'

    def getApiMethod(self):

        return 'suning.invoice.checkresult.query'



