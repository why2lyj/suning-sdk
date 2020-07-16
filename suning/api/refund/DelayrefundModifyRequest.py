# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class DelayrefundModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.refundDetail = None
        self.refundHead = None

    def getApiBizName(self):
        return 'delayRefund'

    def getApiMethod(self):
        return 'suning.custom.delayrefund.modify'

