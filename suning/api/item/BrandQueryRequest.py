# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BrandQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.pageSize = None
        self.brandName = None
        self.targetChannel = None
        self.categoryCode = None
        self.brandCode = None
        self.pageNo = None

    def getApiBizName(self):
        return 'brand'

    def getApiMethod(self):
        return 'suning.custom.brand.query'

