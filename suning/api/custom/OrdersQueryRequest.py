# -*- coding: utf-8 -*-

'''

Created on 2019-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdersQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrders'

    def getApiMethod(self):

        return 'suning.custom.orders.query'



