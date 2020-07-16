# -*- coding: utf-8 -*-

'''

Created on 2015-1-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsCrossbuyInvModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseCode = None
        self.productInv = None



    def getApiBizName(self):

        return 'modifyInventory'



    def getApiMethod(self):

        return 'suning.logistics.crossbuyinventory.modify'



