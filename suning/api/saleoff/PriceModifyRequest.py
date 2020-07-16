# -*- coding: utf-8 -*-

'''

Created on 2018-3-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemCode = None
        self.price = None
        self.productCode = None
        
        self.setParamRule({
        	'price':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyPrice'

    def getApiMethod(self):

        return 'suning.saleoff.price.modify'



