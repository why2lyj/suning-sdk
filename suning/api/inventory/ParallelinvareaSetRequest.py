# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ParallelinvareaSetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invProvinces = None
        self.invCode = None
        self.invCitys = None

    def getApiBizName(self):
        return 'parallelInvarea'

    def getApiMethod(self):
        return 'suning.custom.parallelinvarea.set'

