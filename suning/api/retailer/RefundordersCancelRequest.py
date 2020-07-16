# -*- coding: utf-8 -*-

'''

Created on 2018-8-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundordersCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.merchantCustNo = None
        self.storeCode = None
        self.orderList = None
        self.appId = None
        
        self.setParamRule({
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'appId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelRefundorders'

    def getApiMethod(self):

        return 'suning.retailer.refundorders.cancel'



