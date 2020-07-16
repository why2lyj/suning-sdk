# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoiceinfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.platformCoding = None
        self.requestSeialNum = None
        
        self.setParamRule({
        	'platformCoding':{'allow_empty':False},
        	'requestSeialNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getInvoiceinfo'

    def getApiMethod(self):

        return 'suning.custom.invoiceinfo.get'



