# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class OrdernoteModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.noteContent = None
        self.colorMarkFlag = None
        self.noteFlag = None
        self.orderCode = None

    def getApiBizName(self):
        return 'orderNote'

    def getApiMethod(self):
        return 'suning.custom.ordernote.modify'

