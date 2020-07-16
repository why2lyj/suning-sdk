# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.storeCode = None
        self.appStoreCode = None
        self.operType = None
        self.productList = None
        
        self.setParamRule({
        	'operType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'deleteProduct'

    def getApiMethod(self):

        return 'suning.store.product.delete'



