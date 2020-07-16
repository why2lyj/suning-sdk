# -*- coding: utf-8 -*-

'''

Created on 2019-12-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class InventoryGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityId = None
        self.countyId = None
        self.skuIds = None
        
        self.setParamRule({
        	'cityId':{'allow_empty':False},
        	'countyId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getInventory'

    def getApiMethod(self):

        return 'suning.govbus.inventory.get'



