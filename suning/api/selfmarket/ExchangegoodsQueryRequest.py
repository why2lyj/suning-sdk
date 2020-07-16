# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangegoodsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.exchangeStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.supplierCode = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryExchangegoods'

    def getApiMethod(self):

        return 'suning.selfmarket.exchangegoods.query'



