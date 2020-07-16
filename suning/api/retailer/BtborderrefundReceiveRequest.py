# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtborderrefundReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.channelCode = None
        self.orderItemNo = None
        self.refundState = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'orderItemNo':{'allow_empty':False},
        	'refundState':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receiveBtborderrefund'

    def getApiMethod(self):

        return 'suning.retailer.btborderrefund.receive'



