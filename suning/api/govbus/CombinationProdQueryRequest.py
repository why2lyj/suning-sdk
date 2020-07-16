# -*- coding: utf-8 -*-

'''

Created on 2017-4-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class CombinationProdQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuId = None
        
        self.setParamRule({
        	'skuId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCombinationProd'

    def getApiMethod(self):

        return 'suning.govbus.combinationprod.query'



