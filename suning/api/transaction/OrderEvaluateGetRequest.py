# -*- coding: utf-8 -*-

'''

Created on 2016-5-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderEvaluateGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        self.productCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False},
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrderEvaluate'

    def getApiMethod(self):

        return 'suning.custom.orderevaluate.get'



