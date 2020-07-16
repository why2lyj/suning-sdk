# -*- coding: utf-8 -*-

'''

Created on 2019-8-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class inventoryGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.isNeedLockQty = None
        self.productCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'inventory'

    def getApiMethod(self):

        return 'suning.custom.newinventory.get'



