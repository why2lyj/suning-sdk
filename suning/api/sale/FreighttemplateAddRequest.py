# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class FreighttemplateAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.valuationType = None
        self.continuedValue = None
        self.freightList = None
        self.continuedValueFare = None
        self.shippingType = None
        self.firstValueFare = None
        self.freightTemplateName = None
        self.firstValue = None                self.supplierType = None                self.taxType = None

    def getApiBizName(self):
        return 'freightTemplate'

    def getApiMethod(self):
        return 'suning.custom.freighttemplate.add'

