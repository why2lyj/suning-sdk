# -*- coding: utf-8 -*-

'''

Created on 2017-10-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class UserCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.topicName = None
        
        self.setParamRule({
        	'topicName':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelUser'

    def getApiMethod(self):

        return 'suning.message.user.cancel'



