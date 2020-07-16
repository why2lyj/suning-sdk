# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetNetallianceOrderRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None



    def getApiBizName(self):

        return 'getOrder'



    def getApiMethod(self):

        return 'suning.netalliance.order.get'



