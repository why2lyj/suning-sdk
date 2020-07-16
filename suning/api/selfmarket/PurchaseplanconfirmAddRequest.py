# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurchaseplanconfirmAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.purchasePlanResult = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addPurchaseplan'

    def getApiMethod(self):

        return 'suning.selfmarket.purchaseplanconfirm.add'



