# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class DeliveryReserveAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deliveryHead = None
        self.deliveryDetail = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'deliveryReserve'

    def getApiMethod(self):

        return 'suning.delivery.reserve'



