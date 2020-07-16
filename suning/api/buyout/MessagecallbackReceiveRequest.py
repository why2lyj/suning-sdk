# -*- coding: utf-8 -*-

'''

Created on 2019-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessagecallbackReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.messageId = None
        
        self.setParamRule({
        	'messageId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receiveMessagecallback'

    def getApiMethod(self):

        return 'suning.buyout.messagecallback.receive'



