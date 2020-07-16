# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class InventoryGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseCode = None
        self.commodityCode = None
        self.supplierCommCode = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getInventory'

    def getApiMethod(self):

        return 'suning.swl.inventory.get'



