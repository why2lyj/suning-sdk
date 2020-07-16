# -*- coding: utf-8 -*-

'''

Created on 2020-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessageConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.msgId = None
        self.appId = None
        
        self.setParamRule({
        	'msgId':{'allow_empty':False},
        	'appId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmMessage'

    def getApiMethod(self):

        return 'suning.retailer.message.confirm'



