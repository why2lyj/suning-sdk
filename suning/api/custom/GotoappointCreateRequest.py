# -*- coding: utf-8 -*-

'''

Created on 2020-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class GotoappointCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.actionId = None
        self.custNo = None
        self.partNumber = None
        self.purchaseType = None
        self.storeCode = None
        self.telNo = None
        self.terminalFlag = None
        self.vendorCode = None
        
        self.setParamRule({
        	'actionId':{'allow_empty':False},
        	'custNo':{'allow_empty':False},
        	'partNumber':{'allow_empty':False},
        	'purchaseType':{'allow_empty':False},
        	'telNo':{'allow_empty':False},
        	'terminalFlag':{'allow_empty':False},
        	'vendorCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createGotoappoint'

    def getApiMethod(self):

        return 'suning.custom.gotoappoint.create'



