# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookProductGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.isbnCode = None
        self.productName = None

    def getApiBizName(self):
        return 'product'

    def getApiMethod(self):
        return 'suning.custom.book.product.get'

