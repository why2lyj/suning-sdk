# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetNetallianceOrderSettleRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderLineNumber = None



    def getApiBizName(self):

        return 'getOrderSettle'



    def getApiMethod(self):

        return 'suning.netalliance.ordersettle.get'



