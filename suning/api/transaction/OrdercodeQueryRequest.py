# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class OrdercodeQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.endTime = None
        self.orderStatus = None
        self.startTime = None

    def getApiBizName(self):
        return 'orderCodeQuery'

    def getApiMethod(self):
        return 'suning.custom.ordercode.query'

