# -*- coding: utf-8 -*-

'''

Created on 2020-4-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderbuyConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cardType = None
        self.custNum = None
        self.deviceId = None
        self.ecoType = None
        self.invokerCode = None
        self.orderId = None
        self.orderItem = None
        self.orderSubmitTime = None
        self.sceneType = None
        self.transId = None
        
        self.setParamRule({
        	'cardType':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'ecoType':{'allow_empty':False},
        	'invokerCode':{'allow_empty':False},
        	'orderSubmitTime':{'allow_empty':False},
        	'sceneType':{'allow_empty':False},
        	'transId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmOrderbuy'

    def getApiMethod(self):

        return 'suning.custexpand.orderbuy.confirm'



