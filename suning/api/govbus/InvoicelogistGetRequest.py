# -*- coding: utf-8 -*-

'''

Created on 2019-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoicelogistGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNum = None
        self.parameter = None
        self.parameterInvoice = None
        self.type = None
        
        self.setParamRule({
        	'parameter':{'allow_empty':False},
        	'type':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getInvoicelogist'

    def getApiMethod(self):

        return 'suning.govbus.invoicelogist.get'



