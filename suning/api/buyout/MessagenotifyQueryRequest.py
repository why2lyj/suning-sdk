# -*- coding: utf-8 -*-

'''

Created on 2019-10-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessagenotifyQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.messageType = None
        
        self.setParamRule({
        	'messageType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryMessagenotify'

    def getApiMethod(self):

        return 'suning.buyout.messagenotify.query'



