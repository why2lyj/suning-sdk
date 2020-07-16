# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class SinglerejectedGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.orderCode = None

    def getApiBizName(self):
        return 'singleGetRejected'

    def getApiMethod(self):
        return 'suning.custom.singlerejected.get'

