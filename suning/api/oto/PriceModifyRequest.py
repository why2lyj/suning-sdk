# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.physicalCode = None
        self.productCode = None
        self.itemCode = None
        self.price = None
        
        self.setParamRule({
        	'physicalCode':{'allow_empty':False},
        	'price':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyPrice'

    def getApiMethod(self):

        return 'suning.oto.price.modify'



