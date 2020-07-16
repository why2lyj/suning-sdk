# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class BatchrejectedQueryRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.pageSize = None
        self.endTime = None
        self.pageNo = None
        self.startTime = None

    def getApiBizName(self):
        return 'batchQueryRejected'

    def getApiMethod(self):
        return 'suning.custom.batchrejected.query'

