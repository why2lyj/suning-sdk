# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class BatchProdSaleStatusGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityId = None
        self.skuIds = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getBatchProdSaleStatus'

    def getApiMethod(self):

        return 'suning.govbus.batchprodsalestatus.get'



