# -*- coding: utf-8 -*-

'''

Created on 2017-3-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProdReviewQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuIds = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryProdReview'

    def getApiMethod(self):

        return 'suning.govbus.prodreview.query'



