# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ItemGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.productName = None
        self.cmTitle = None
    def getApiBizName(self):
        return 'item'

    def getApiMethod(self):
        return 'suning.custom.item.get'

