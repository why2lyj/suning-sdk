# -*- coding: utf-8 -*-

'''

Created on 2015-2-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'orderGet'

    def getApiMethod(self):

        return 'suning.custom.order.get'



