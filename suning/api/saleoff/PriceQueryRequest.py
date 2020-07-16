# -*- coding: utf-8 -*-

'''

Created on 2018-3-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemCode = None
        self.productCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryPrice'

    def getApiMethod(self):

        return 'suning.saleoff.price.query'



