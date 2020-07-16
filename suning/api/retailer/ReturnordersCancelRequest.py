# -*- coding: utf-8 -*-

'''

Created on 2018-9-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReturnordersCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.merchantCustNo = None
        self.storeCode = None
        self.orderNo = None
        self.orderItemNo = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'orderNo':{'allow_empty':False},
        	'orderItemNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelReturnorders'

    def getApiMethod(self):

        return 'suning.retailer.returnorders.cancel'



