# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class InvaddressAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.streetAddress = None
        self.invContact = None
        self.invName = None
        self.invRegion = None
        self.remark = None
        self.invCity = None
        self.phoneNum = None
        self.zipCode = None
        self.invProvince = None
        self.telePhone = None

    def getApiBizName(self):
        return 'invaddress'

    def getApiMethod(self):
        return 'suning.custom.invaddress.add'

