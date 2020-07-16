# -*- coding: utf-8 -*-

'''

Created on 2020-6-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommodityimagesQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commodityCode = None
        self.supplierCode = None
        self.terminalType = None
        
        self.setParamRule({
        	'commodityCode':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCommodityimages'

    def getApiMethod(self):

        return 'suning.netalliance.commodityimages.query'



