# -*- coding: utf-8 -*-

'''

Created on 2018-3-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class itemSaleQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.cmTitle = None
        self.pageNo = None
        self.pageSize = None
        self.productCode = None
        self.productName = None
        self.saleStatus = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'itemSale'

    def getApiMethod(self):

        return 'suning.integrate.itemsale.query'



