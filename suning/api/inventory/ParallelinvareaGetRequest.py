# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ParallelinvareaGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invCode = None

    def getApiBizName(self):
        return 'parallelInvarea'

    def getApiMethod(self):
        return 'suning.custom.parallelinvarea.get'

