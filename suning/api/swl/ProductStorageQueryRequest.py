# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductStorageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.orderState = None
        self.warehouseCode = None
        self.orderBeginDate = None
        self.orderEndDate = None
        self.applyBeginDate = None
        self.applyEndDate = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryProductStorage'

    def getApiMethod(self):

        return 'suning.swl.productstorage.query'



