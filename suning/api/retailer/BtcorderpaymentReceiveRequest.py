# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtcorderpaymentReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.orderCode = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receiveBtcorderpayment'

    def getApiMethod(self):

        return 'suning.retailer.btcorderpayment.receive'



