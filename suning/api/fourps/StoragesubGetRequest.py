# -*- coding: utf-8 -*-

'''

Created on 2016-5-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoragesubGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.purchaseOrderId = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getStoragesub'

    def getApiMethod(self):

        return 'suning.fourps.storagesub.get'



