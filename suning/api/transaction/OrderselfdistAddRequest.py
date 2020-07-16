# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderselfdistAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        self.deliveryPerName = None
        self.deliveryPerPhone = None
        self.deliveryTime = None
        self.productCodes = None
        self.orderLineNumbers = None



    def getApiBizName(self):

        return 'orderSelfDist'



    def getApiMethod(self):

        return 'suning.custom.orderselfdist.add'



