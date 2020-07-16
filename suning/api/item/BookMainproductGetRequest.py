# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BookMainproductGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.applyCode = None

    def getApiBizName(self):
        return 'mainProduct'

    def getApiMethod(self):
        return 'suning.custom.book.mainproduct.get'

