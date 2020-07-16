# -*- coding: utf-8 -*-

'''

Created on 2019-9-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class SettlementpriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyInfo = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'querySettlementprice'

    def getApiMethod(self):

        return 'suning.online.settlementprice.query'



