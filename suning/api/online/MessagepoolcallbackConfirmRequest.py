# -*- coding: utf-8 -*-

'''

Created on 2019-10-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessagepoolcallbackConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.messageList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmMessagepoolcallback'

    def getApiMethod(self):

        return 'suning.online.messagepoolcallback.confirm'



