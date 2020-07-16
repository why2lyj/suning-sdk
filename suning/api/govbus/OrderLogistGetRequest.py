# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderLogistGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItemId = None
        self.skuId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'skuId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderLogist'

    def getApiMethod(self):

        return 'suning.govbus.orderlogist.get'



