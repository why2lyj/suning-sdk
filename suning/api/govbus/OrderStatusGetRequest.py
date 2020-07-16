# -*- coding: utf-8 -*-

'''

Created on 2018-2-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderStatusGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderStatus'

    def getApiMethod(self):

        return 'suning.govbus.orderstatus.get'



