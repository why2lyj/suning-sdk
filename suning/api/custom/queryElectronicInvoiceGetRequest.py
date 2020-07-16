# -*- coding: utf-8 -*-

'''

Created on 2019-3-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class queryElectronicInvoiceGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.productCode = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryElectronicInvoice'

    def getApiMethod(self):

        return 'suning.custom.electronicinvoice.get'



