# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydbtborderinvoiceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.ivcType = None
        self.orderId = None
        self.queryExts = None
        self.token = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryJsydbtborderinvoice'

    def getApiMethod(self):

        return 'suning.retailer.jsydbtborderinvoice.query'



