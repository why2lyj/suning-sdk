# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtborderpayReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.orderAmount = None
        self.orderNo = None
        self.payBankAccount = None
        self.payBankName = None
        self.payBankNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'orderAmount':{'allow_empty':False},
        	'orderNo':{'allow_empty':False},
        	'payBankNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receiveBtborderpay'

    def getApiMethod(self):

        return 'suning.retailer.btborderpay.receive'



