# -*- coding: utf-8 -*-

'''

Created on 2015-12-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class StockFormQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.placeCode = None
        self.pageNo = None
        self.pageSize = None
        self.brandCode = None
        
        self.setParamRule({
        	'brandCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryStockForm'

    def getApiMethod(self):

        return 'suning.selfmarket.stockform.query'



