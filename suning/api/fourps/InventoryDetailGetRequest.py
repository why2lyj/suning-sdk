# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class InventoryDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commodityCode = None
        self.commodityName = None
        self.colourNumber = None
        self.batchNumber = None
        self.serviceProvider = None
        self.warehouseCode = None
        self.platformCode = None
        
        self.setParamRule({
        	'commodityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getInventoryDetail'

    def getApiMethod(self):

        return 'suning.fourps.inventorydetail.get'



