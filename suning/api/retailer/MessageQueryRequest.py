# -*- coding: utf-8 -*-

'''

Created on 2020-2-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryMessage'

    def getApiMethod(self):

        return 'suning.retailer.message.query'



