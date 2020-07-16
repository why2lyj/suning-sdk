# -*- coding: utf-8 -*-

'''

Created on 2020-3-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class orderDeliveryAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deliveryTime = None
        self.expressCompanyCode = None
        self.expressNo = None
        self.orderCode = None
        self.orderLineNumbers = None
        self.phoneIdentifyCodes = None
        self.sendDetail = None
        
        self.setParamRule({
        	'expressCompanyCode':{'allow_empty':False},
        	'expressNo':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'orderDelivery'

    def getApiMethod(self):

        return 'suning.custom.orderdelivery.add'



