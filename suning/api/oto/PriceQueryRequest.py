# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.physicalCode = None
        self.itemCode = None
        
        self.setParamRule({
        	'physicalCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryPrice'

    def getApiMethod(self):

        return 'suning.oto.price.query'



