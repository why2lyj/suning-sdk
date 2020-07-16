# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ShelvesMoveRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None

    def getApiBizName(self):
        return 'shelves'

    def getApiMethod(self):
        return 'suning.custom.shelves.move'

