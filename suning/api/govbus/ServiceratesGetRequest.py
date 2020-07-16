# -*- coding: utf-8 -*-

'''

Created on 2019-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class ServiceratesGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItemIds = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getServicerates'

    def getApiMethod(self):

        return 'suning.govbus.servicerates.get'



