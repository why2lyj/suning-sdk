# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangegoodsdeliveryUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.exchangeNo = None
        self.sign = None
        self.expressCompCode = None
        self.expressNo = None
        self.sender = None
        self.senderTel = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	'exchangeNo':{'allow_empty':False},
        	'sign':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'updateExchangegoodsdelivery'

    def getApiMethod(self):

        return 'suning.selfmarket.exchangegoodsdelivery.update'



