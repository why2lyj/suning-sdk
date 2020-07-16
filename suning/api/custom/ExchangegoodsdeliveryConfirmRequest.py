# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangegoodsdeliveryConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.changeApplyId = None
        self.deExpressCompanyCode = None
        self.deExpressno = None
        
        self.setParamRule({
        	'changeApplyId':{'allow_empty':False},
        	'deExpressCompanyCode':{'allow_empty':False},
        	'deExpressno':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmExchangegoodsdelivery'

    def getApiMethod(self):

        return 'suning.custom.exchangegoodsdelivery.confirm'



