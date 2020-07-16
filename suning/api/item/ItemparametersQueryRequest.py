# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ItemparametersQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.categoryCode = None
        self.pageSize = None
        self.pageNo = None
        self.targetChannel = None

    def getApiBizName(self):
        return 'itemParameters'

    def getApiMethod(self):
        return 'suning.custom.itemparameters.query'

