# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class DisagreerejectedModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.rejectedHead = None
        self.rejectedDetail = None

    def getApiBizName(self):
        return 'disAgreeRejected'

    def getApiMethod(self):
        return 'suning.custom.disagreerejected.modify'

