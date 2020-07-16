# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class CustOpinionGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chatId = None
        
        self.setParamRule({
        	'chatId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCustOpinion'

    def getApiMethod(self):

        return 'suning.cloudinfo.custopinion.get'



