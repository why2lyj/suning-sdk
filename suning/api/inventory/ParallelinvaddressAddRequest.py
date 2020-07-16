# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class ParallelinvaddressAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invCode = None
        self.invNameBack = None
        self.invContact = None
        self.invName = None
        self.invRegion = None
        self.invCity = None
        self.phoneNum = None
        self.streetAddress = None
        self.invProvince = None
        self.zipCode = None

    def getApiBizName(self):
        return 'parallelInvaddress'

    def getApiMethod(self):
        return 'suning.custom.parallelinvaddress.add'

