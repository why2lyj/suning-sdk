# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookProductdetailQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None

    def getApiBizName(self):
        return 'productDetail'

    def getApiMethod(self):
        return 'suning.custom.book.productdetail.query'

