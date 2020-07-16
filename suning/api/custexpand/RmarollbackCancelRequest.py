# -*- coding: utf-8 -*-

'''

Created on 2020-4-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class RmarollbackCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appCode = None
        self.branch = None
        self.custNum = None
        self.ecoType = None
        self.handlers = None
        self.isCalcTotalOffsetLimit = None
        self.orderItemId = None
        self.orderType = None
        self.sourceChannel = None
        self.sourceSystemNo = None
        self.store = None
        self.tranTimestamp = None
        self.uniteOrderId = None
        
        self.setParamRule({
        	'appCode':{'allow_empty':False},
        	'branch':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'ecoType':{'allow_empty':False},
        	'handlers':{'allow_empty':False},
        	'sourceChannel':{'allow_empty':False},
        	'sourceSystemNo':{'allow_empty':False},
        	'store':{'allow_empty':False},
        	'tranTimestamp':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'cancelRmarollback'

    def getApiMethod(self):

        return 'suning.custexpand.rmarollback.cancel'



