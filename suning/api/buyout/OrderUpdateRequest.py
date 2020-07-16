# -*- coding: utf-8 -*-

'''

Created on 2019-10-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateOrder'

    def getApiMethod(self):

        return 'suning.buyout.order.update'



