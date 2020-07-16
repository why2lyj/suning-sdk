# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class OrdercountdownQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.countDown = None
        self.orderLineNumbers = None
        self.orderCode = None

    def getApiBizName(self):
        return 'orderCountDown'

    def getApiMethod(self):
        return 'suning.custom.ordercountdown.query'

