# -*- coding: utf-8 -*-

'''

Created on 2020-1-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItems = None
        self.orderStatus = None
        self.payDate = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'orderStatus':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'updateOrder'

    def getApiMethod(self):

        return 'suning.online.order.update'



