# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class CategoryQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.pageSize = None
        self.pageNo = None
        self.categoryName = None
        self.targetChannel = None

    def getApiBizName(self):
        return 'category'

    def getApiMethod(self):
        return 'suning.custom.category.query'

