# -*- coding: utf-8 -*-

'''

Created on 2020-4-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdersettlenewGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderLineNumber = None
        
        self.setParamRule({
        	'orderLineNumber':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrdersettlenew'

    def getApiMethod(self):

        return 'suning.netalliance.ordersettlenew.get'



