# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApi

class InventoryModifyRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)
        self.productCode = None
        self.itemCode = None
        self.invAddrId = None
        self.destInvNum = None
        self.invType = None
    def getApiBizName(self):
        return 'inventory'

    def getApiMethod(self):
        return 'suning.custom.inventory.modify'

