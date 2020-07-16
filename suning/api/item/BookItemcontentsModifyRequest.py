# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookItemcontentsModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.saleSet = None
        self.sellPoint = None
        self.itemCode = None
        self.afterSaleServiceDec = None
        self.freightTemplateId = None
        self.saleDate = None
    def getApiBizName(self):
        return 'itemContents'

    def getApiMethod(self):
        return 'suning.custom.book.itemcontents.modify'
