# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class DisagreerefundModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.refundDetail = None
        self.refundHead = None

    def getApiBizName(self):
        return 'disAgreeRefund'

    def getApiMethod(self):
        return 'suning.custom.disagreerefund.modify'

