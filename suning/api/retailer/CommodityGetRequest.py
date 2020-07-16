# -*- coding: utf-8 -*-

'''

Created on 2018-11-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommodityGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyCode = None
        self.appId = None
        self.storeCode = None
        self.merchantCustNo = None
        
        self.setParamRule({
        	'cmmdtyCode':{'allow_empty':False},
        	'appId':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCommodity'

    def getApiMethod(self):

        return 'suning.retailer.commodity.get'



