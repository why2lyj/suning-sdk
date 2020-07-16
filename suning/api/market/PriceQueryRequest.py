# -*- coding: utf-8 -*-

'''

Created on 2019-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPrice'

    def getApiMethod(self):

        return 'suning.market.price.query'



