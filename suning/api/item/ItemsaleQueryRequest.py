# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ItemsaleQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.categoryCode = None
        self.saleStatus = None
        self.pageNo = None
        self.pageSize = None
        self.priceUpper = None
        self.priceLimit = None
        self.productName = None
        self.cmTitle = None
    def getApiBizName(self):
        return 'itemSale'

    def getApiMethod(self):
        return 'suning.custom.itemsale.query'

