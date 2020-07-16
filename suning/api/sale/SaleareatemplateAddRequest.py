# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class SaleareatemplateAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.nation = None
        self.provList = None
        self.cityList = None
        self.templateName = None

    def getApiBizName(self):
        return 'saleAreaTemplate'

    def getApiMethod(self):
        return 'suning.custom.saleareatemplate.add'

