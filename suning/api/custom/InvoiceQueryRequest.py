# -*- coding: utf-8 -*-

'''

Created on 2019-12-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoiceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderNum = None
        self.pageNum = None
        self.pageRow = None
        self.platformCoding = None
        self.requestSeialNum = None
        
        self.setParamRule({
        	'platformCoding':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryInvoice'

    def getApiMethod(self):

        return 'suning.custom.invoice.query'



