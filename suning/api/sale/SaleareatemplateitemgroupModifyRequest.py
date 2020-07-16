# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class SaleareatemplateitemgroupModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.grade = None
        self.lineComGroupInfoList = None
        self.templateId = None

    def getApiBizName(self):
        return 'saleAreaTemplateItemGroup'

    def getApiMethod(self):
        return 'suning.custom.saleareatemplateitemgroup.modify'

