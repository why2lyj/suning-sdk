# -*- coding: utf-8 -*-

'''

Created on 2017-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class UserPermitRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.topicName = None
        
        self.setParamRule({
        	'topicName':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'permitUser'

    def getApiMethod(self):

        return 'suning.message.user.permit'



