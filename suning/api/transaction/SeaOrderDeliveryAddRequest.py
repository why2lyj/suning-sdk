# -*- coding: utf-8 -*-

'''

Created on 2019-1-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class SeaOrderDeliveryAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deliveryDetails = None
        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'seaOrderDelivery'

    def getApiMethod(self):

        return 'suning.custom.seaorderdelivery.add'



