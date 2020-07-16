# -*- coding: utf-8 -*-

'''

Created on 2018-8-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class DeliveryorderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deliveryDetail = None
        self.deliveryHead = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addDeliveryorder'

    def getApiMethod(self):

        return 'suning.selfmarket.deliveryorder.add'



