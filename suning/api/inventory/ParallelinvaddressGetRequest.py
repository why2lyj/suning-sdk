# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ParallelinvaddressGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invCode = None

    def getApiBizName(self):
        return 'parallelInvaddress'

    def getApiMethod(self):
        return 'suning.custom.parallelinvaddress.get'

