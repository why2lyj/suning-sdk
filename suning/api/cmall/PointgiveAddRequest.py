# -*- coding: utf-8 -*-

'''

Created on 2017-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class PointgiveAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        self.deviceId = None
        self.ecoType = None
        self.invokerCode = None
        self.order = None
        self.orderId = None
        self.sceneCode = None
        self.sceneType = None
        self.transId = None
        self.transTimestamp = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False},
        	'ecoType':{'allow_empty':False},
        	'invokerCode':{'allow_empty':False},
        	'sceneCode':{'allow_empty':False},
        	'sceneType':{'allow_empty':False},
        	'transId':{'allow_empty':False},
        	'transTimestamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPointgive'

    def getApiMethod(self):

        return 'suning.cmall.pointgive.add'



