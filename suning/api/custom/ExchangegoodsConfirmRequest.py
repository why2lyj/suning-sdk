# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangegoodsConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.changeApplyId = None
        self.invAddrId = None
        self.remark = None
        
        self.setParamRule({
        	'changeApplyId':{'allow_empty':False},
        	'invAddrId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'confirmExchangegoods'

    def getApiMethod(self):

        return 'suning.custom.exchangegoods.confirm'



