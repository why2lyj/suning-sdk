# -*- coding: utf-8 -*-

'''

Created on 2018-2-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgentrechargeGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelId = None
        self.reqSerial = None
        self.reqTime = None
        self.serialNumber = None
        self.reqSign = None
        
        self.setParamRule({
        	'channelId':{'allow_empty':False},
        	'reqSerial':{'allow_empty':False},
        	'reqTime':{'allow_empty':False},
        	'serialNumber':{'allow_empty':False},
        	'reqSign':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getAgentrecharge'

    def getApiMethod(self):

        return 'suning.operasale.agentrecharge.get'



