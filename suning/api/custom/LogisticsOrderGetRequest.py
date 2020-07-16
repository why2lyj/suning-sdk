# -*- coding: utf-8 -*-

'''

Created on 2017-6-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsOrderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.logisticExpressId = None
        self.logisticOrderId = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getLogisticsOrder'

    def getApiMethod(self):

        return 'suning.custom.logisticsorder.get'



