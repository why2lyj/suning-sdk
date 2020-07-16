# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deductiblePrice = None
        self.itemCode = None
        self.price = None
        self.productCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'updatePrice'

    def getApiMethod(self):

        return 'suning.custom.price.update'



