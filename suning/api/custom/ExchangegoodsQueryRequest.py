# -*- coding: utf-8 -*-

'''

Created on 2020-4-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExchangegoodsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.changeApplyIds = None
        self.changeStatus = None
        self.endModified = None
        self.pageNo = None
        self.pageSize = None
        self.startModified = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryExchangegoods'

    def getApiMethod(self):

        return 'suning.custom.exchangegoods.query'



