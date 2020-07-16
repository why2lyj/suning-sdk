# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydcmmdtycartsourcingQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.area = None
        self.skuNums = None
        self.token = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryJsydcmmdtycartsourcing'

    def getApiMethod(self):

        return 'suning.retailer.jsydcmmdtycartsourcing.query'



