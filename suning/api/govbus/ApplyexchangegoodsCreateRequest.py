# -*- coding: utf-8 -*-

'''

Created on 2019-9-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApplyexchangegoodsCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItems = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createApplyexchangegoods'

    def getApiMethod(self):

        return 'suning.govbus.applyexchangegoods.create'



