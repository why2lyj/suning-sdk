# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class OrderdeliveryModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.expressNo = None
        self.orderLineNumbers = None
        self.expressCompanyCode = None
        self.orderCode = None
        self.sendDetail = None

    def getApiBizName(self):
        return 'orderDelivery'

    def getApiMethod(self):
        return 'suning.custom.orderdelivery.modify'

