# -*- coding: utf-8 -*-

'''

Created on 2016-11-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromKeywordMarketQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.catalogSecond = None
        self.catalogThird = None
        
        self.setParamRule({
        	'catalogSecond':{'allow_empty':False},
        	'catalogThird':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPromKeywordMarket'

    def getApiMethod(self):

        return 'suning.advertise.promkeywordmarket.query'



