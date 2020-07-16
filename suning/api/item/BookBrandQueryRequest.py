# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookBrandQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.pageSize = None
        self.brandName = None
        self.brandCode = None
        self.pageNo = None

    def getApiBizName(self):
        return 'brand'

    def getApiMethod(self):
        return 'suning.custom.book.brand.query'

