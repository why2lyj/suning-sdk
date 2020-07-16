# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BatchrejectedordQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.endTime = None
        self.startTime = None

    def getApiBizName(self):
        return 'batchQueryRejectedOrd'

    def getApiMethod(self):
        return 'suning.custom.batchrejectedOrd.query'

