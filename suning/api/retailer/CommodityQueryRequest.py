# -*- coding: utf-8 -*-

'''

Created on 2019-4-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommodityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.cmmdtyCode = None
        self.distributorCode = None
        self.merchantCustNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'cmmdtyCode':{'allow_empty':False},
        	'distributorCode':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCommodity'

    def getApiMethod(self):

        return 'suning.retailer.commodity.query'



