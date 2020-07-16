# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderDetail'

    def getApiMethod(self):

        return 'suning.govbus.orderdetail.get'



