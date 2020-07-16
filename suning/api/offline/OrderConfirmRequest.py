# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.counterCode = None
        self.orderAmount = None
        self.payId = None
        self.payItemInfo = None
        self.payTime = None
        self.rtStoreCode = None
        self.verifyCode = None
        
        self.setParamRule({
        	'orderAmount':{'allow_empty':False},
        	'payId':{'allow_empty':False},
        	'payTime':{'allow_empty':False},
        	'rtStoreCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'confirmOrder'

    def getApiMethod(self):

        return 'suning.offline.order.confirm'



