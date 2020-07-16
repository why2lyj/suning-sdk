# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class parallelInventoryGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.invCode = None
        self.isNeedLockQty = None
        self.itemCode = None
        self.productCode = None
        
        self.setParamRule({
        	'invCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'parallelInventory'

    def getApiMethod(self):

        return 'suning.custom.parallelinventory.get'



