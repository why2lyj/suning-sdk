# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductinventoryModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.storeCode = None
        self.appStoreCode = None
        self.productCode = None
        self.qty = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'qty':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyProductinventory'

    def getApiMethod(self):

        return 'suning.store.productinventory.modify'



