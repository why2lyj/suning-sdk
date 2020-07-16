# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class InvaddressGetRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invAddrId = None

    def getApiBizName(self):
        return 'invaddress'

    def getApiMethod(self):
        return 'suning.custom.invaddress.get'

