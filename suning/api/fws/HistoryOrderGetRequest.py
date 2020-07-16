# -*- coding: utf-8 -*-

'''

Created on 2015-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class HistoryOrderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderDetailId = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getHistoryOrder'

    def getApiMethod(self):

        return 'suning.fws.historyorder.get'



