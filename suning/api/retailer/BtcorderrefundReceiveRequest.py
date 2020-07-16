# -*- coding: utf-8 -*-

'''

Created on 2020-4-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtcorderrefundReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.orderCode = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receiveBtcorderrefund'

    def getApiMethod(self):

        return 'suning.retailer.btcorderrefund.receive'



