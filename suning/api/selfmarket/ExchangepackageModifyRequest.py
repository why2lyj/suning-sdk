# -*- coding: utf-8 -*-

'''

Created on 2019-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangepackageModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.exchangeNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	'exchangeNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyExchangepackage'

    def getApiMethod(self):

        return 'suning.selfmarket.exchangepackage.modify'



