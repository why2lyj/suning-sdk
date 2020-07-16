# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtcorderprepaymentConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.checkType = None
        self.orderCode = None
        self.storeCode = None
        self.channelCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'checkType':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'confirmBtcorderprepayment'

    def getApiMethod(self):

        return 'suning.retailer.btcorderprepayment.confirm'



