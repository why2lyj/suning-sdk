# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class TransportGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemId = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getTransport'

    def getApiMethod(self):

        return 'suning.online.transport.get'



