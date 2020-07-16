# -*- coding: utf-8 -*-

'''

Created on 2018-8-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.storeCode = None
        self.merchantCustNo = None
        self.salesMode = None
        self.cmmdtyList = None
        self.timestamp = None
        self.appId = None
        
        self.setParamRule({
        	'storeCode':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'timestamp':{'allow_empty':False},
        	'appId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updatePrice'

    def getApiMethod(self):

        return 'suning.retailer.price.update'



