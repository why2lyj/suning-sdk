# -*- coding: utf-8 -*-

'''

Created on 2020-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class EleinvoiceGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItems = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getEleinvoice'

    def getApiMethod(self):

        return 'suning.govbus.eleinvoice.get'



