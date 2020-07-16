# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class SaleareatemplateDeleteRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.templateId = None

    def getApiBizName(self):
        return 'saleAreaTemplate'

    def getApiMethod(self):
        return 'suning.custom.saleareatemplate.delete'

