# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class InventoryQuantityGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commodityCode = None
        self.colourNumber = None
        self.batchNumber = None
        
        self.setParamRule({
        	'commodityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getInventoryQuantity'

    def getApiMethod(self):

        return 'suning.fourps.inventoryquantity.get'



