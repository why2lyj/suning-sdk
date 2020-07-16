# -*- coding: utf-8 -*-

'''

Created on 2017-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ResultAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.expressKey = None
        self.failReason = None
        self.freight = None
        self.pickupMan = None
        self.pickupManContact = None
        self.pickupNetwork = None
        self.pickupNetworkContact = None
        self.pickupState = None
        self.pickupTime = None
        self.pushType = None
        self.returnOrderId = None
        self.signupState = None
        self.signupTime = None
        self.waybillNo = None
        self.weight = None
        
        self.setParamRule({
        	'expressKey':{'allow_empty':False},
        	'pushType':{'allow_empty':False},
        	'returnOrderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addResult'

    def getApiMethod(self):

        return 'suning.fourps.result.add'



