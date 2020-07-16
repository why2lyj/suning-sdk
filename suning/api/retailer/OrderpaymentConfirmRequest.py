# -*- coding: utf-8 -*-

'''

Created on 2018-8-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderpaymentConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.merchantCustNo = None
        self.storeCode = None
        self.orderNo = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'orderNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmOrderpayment'

    def getApiMethod(self):

        return 'suning.retailer.orderpayment.confirm'



