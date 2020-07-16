# -*- coding: utf-8 -*-

'''

Created on 2016-2-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderRelGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.userId = None
        self.itemcode = None
        self.orderId = None
        
        self.setParamRule({
        	'userId':{'allow_empty':False},
        	'itemcode':{'allow_empty':False},
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderRel'

    def getApiMethod(self):

        return 'suning.cloud.orderrel.get'



