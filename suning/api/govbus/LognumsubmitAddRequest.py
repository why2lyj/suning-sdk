# -*- coding: utf-8 -*-

'''

Created on 2019-7-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class LognumsubmitAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItemIds = None
        self.serviceType = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'serviceType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addLognumsubmit'

    def getApiMethod(self):

        return 'suning.govbus.lognumsubmit.add'



