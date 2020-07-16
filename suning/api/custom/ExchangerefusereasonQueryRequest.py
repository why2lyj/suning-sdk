# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangerefusereasonQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.changeReasonType = None
        
        self.setParamRule({
        	'changeReasonType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryExchangerefusereason'

    def getApiMethod(self):

        return 'suning.custom.exchangerefusereason.query'



