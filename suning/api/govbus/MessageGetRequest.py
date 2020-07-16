# -*- coding: utf-8 -*-

'''

Created on 2020-4-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessageGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.type = None
        
        self.setParamRule({
        	'type':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getMessage'

    def getApiMethod(self):

        return 'suning.govbus.message.get'



