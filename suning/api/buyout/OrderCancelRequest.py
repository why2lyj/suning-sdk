# -*- coding: utf-8 -*-

'''

Created on 2019-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.flag = None
        self.orderId = None
        
        self.setParamRule({
        	'flag':{'allow_empty':False},
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelOrder'

    def getApiMethod(self):

        return 'suning.buyout.order.cancel'



