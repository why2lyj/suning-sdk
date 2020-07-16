# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookItemdetailQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.itemCode = None

    def getApiBizName(self):
        return 'itemDetail'

    def getApiMethod(self):
        return 'suning.custom.book.itemdetail.query'

