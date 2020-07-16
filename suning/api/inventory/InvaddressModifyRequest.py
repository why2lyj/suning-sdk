# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class InvaddressModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.invName = None
        self.phoneNum = None
        self.zipCode = None
        self.invRegion = None
        self.invAddrId = None
        self.remark = None
        self.invContact = None
        self.telePhone = None
        self.streetAddress = None
        self.invCity = None
        self.invProvince = None

    def getApiBizName(self):
        return 'invaddress'

    def getApiMethod(self):
        return 'suning.custom.invaddress.modify'

