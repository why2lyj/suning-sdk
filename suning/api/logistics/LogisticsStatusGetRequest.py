# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsStatusGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.logisticOrderId = None
        self.logisticExpressId = None



    def getApiBizName(self):

        return 'getLogisticsStatus'



    def getApiMethod(self):

        return 'suning.custom.logisticsstatus.get'



