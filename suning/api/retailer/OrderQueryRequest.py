# -*- coding: utf-8 -*-

'''

Created on 2018-11-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderNo = None
        self.merchantCustNo = None
        self.storeCode = None
        self.appId = None
        self.orderItemNo = None
        
        self.setParamRule({
        	'orderNo':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrder'

    def getApiMethod(self):

        return 'suning.retailer.purchaseorders.query'



