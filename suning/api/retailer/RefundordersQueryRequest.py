# -*- coding: utf-8 -*-

'''

Created on 2018-8-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundordersQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderNo = None
        self.orderItemNo = None
        self.merchantCustNo = None
        self.storeCode = None
        self.appId = None
        
        self.setParamRule({
        	'orderNo':{'allow_empty':False},
        	'orderItemNo':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'appId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRefundorders'

    def getApiMethod(self):

        return 'suning.retailer.refundorders.query'



