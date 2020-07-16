# -*- coding: utf-8 -*-

'''

Created on 2019-4-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class OnlinepayCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.backUrl = None
        self.channelType = None
        self.orderId = None
        
        self.setParamRule({
        	'backUrl':{'allow_empty':False},
        	'channelType':{'allow_empty':False},
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createOnlinepay'

    def getApiMethod(self):

        return 'suning.govbus.onlinepay.create'



