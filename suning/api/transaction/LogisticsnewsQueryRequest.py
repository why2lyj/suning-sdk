# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class LogisticsnewsQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.logisticCode = None
        self.waybillNo = None

    def getApiBizName(self):
        return 'logisticsnews'

    def getApiMethod(self):
        return 'suning.custom.logisticsnews.query'

