# -*- coding: utf-8 -*-

'''

Created on 2020-4-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class PointlockCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accountStruct = None
        self.appCode = None
        self.beginRecNum = None
        self.custNum = None
        self.ecoType = None
        self.getRecNum = None
        self.sourceChannel = None
        self.sourceSystemNo = None
        self.tranTimestamp = None
        
        self.setParamRule({
        	'appCode':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'ecoType':{'allow_empty':False},
        	'sourceChannel':{'allow_empty':False},
        	'sourceSystemNo':{'allow_empty':False},
        	'tranTimestamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelPointlock'

    def getApiMethod(self):

        return 'suning.custexpand.pointlock.cancel'



