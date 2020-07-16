# -*- coding: utf-8 -*-

'''

Created on 2016-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductRealStorageGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getProductRealStorage'

    def getApiMethod(self):

        return 'suning.swl.productrealstorage.get'



