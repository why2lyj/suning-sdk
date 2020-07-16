# -*- coding: utf-8 -*-

'''

Created on 2018-2-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgentrechargeAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelId = None
        self.serialNumber = None
        self.feeAmount = None
        self.reqSerial = None
        self.reqTime = None
        self.reqSign = None
        
        self.setParamRule({
        	'channelId':{'allow_empty':False},
        	'serialNumber':{'allow_empty':False},
        	'feeAmount':{'allow_empty':False},
        	'reqSerial':{'allow_empty':False},
        	'reqTime':{'allow_empty':False},
        	'reqSign':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addAgentrecharge'

    def getApiMethod(self):

        return 'suning.operasale.agentrecharge.add'



