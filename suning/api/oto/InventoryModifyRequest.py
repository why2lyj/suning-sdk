# -*- coding: utf-8 -*-

'''

Created on 2018-4-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class InventoryModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.shopCode = None
        self.productCode = None
        self.itemCode = None
        self.invQty = None
        
        self.setParamRule({
        	'shopCode':{'allow_empty':False},
        	'invQty':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyInventory'

    def getApiMethod(self):

        return 'suning.oto.inventory.modify'



