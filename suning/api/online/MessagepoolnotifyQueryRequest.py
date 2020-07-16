# -*- coding: utf-8 -*-

'''

Created on 2020-3-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessagepoolnotifyQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.messageType = None
        
        self.setParamRule({
        	'messageType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryMessagepoolnotify'

    def getApiMethod(self):

        return 'suning.online.messagepoolnotify.query'



