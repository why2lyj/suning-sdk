# -*- coding: utf-8 -*-

'''

Created on 2018-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class itemSaleQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.productName = None
        self.productCode = None
        self.categoryCode = None
        self.priceUpper = None
        self.priceLimit = None
        self.saleStatus = None
        self.cmTitle = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'itemSale'

    def getApiMethod(self):

        return 'suning.custom.itemsale.query'



