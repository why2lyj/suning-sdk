# -*- coding: utf-8 -*-

'''

Created on 2017-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class MylibaryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.productName = None
        self.itemCode = None
        self.cmTitle = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryMylibary'

    def getApiMethod(self):

        return 'suning.saleoff.mylibary.query'



