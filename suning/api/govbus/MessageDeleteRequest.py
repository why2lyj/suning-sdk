# -*- coding: utf-8 -*-

'''

Created on 2020-4-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessageDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.id = None
        
        self.setParamRule({
        	'id':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteMessage'

    def getApiMethod(self):

        return 'suning.govbus.message.delete'



