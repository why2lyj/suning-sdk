# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydbtborderpayReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.companyPayMoney = None
        self.orderId = None
        self.payBankAccount = None
        self.payBankName = None
        self.payBankNo = None
        self.token = None
        
        self.setParamRule({
        	'companyPayMoney':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'payBankAccount':{'allow_empty':False},
        	'payBankNo':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receiveJsydbtborderpay'

    def getApiMethod(self):

        return 'suning.retailer.jsydbtborderpay.receive'



