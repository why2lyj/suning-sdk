# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class QueryNetallianceOrderRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.orderLineStatus = None



    def getApiBizName(self):

        return 'queryOrder'



    def getApiMethod(self):

        return 'suning.netalliance.order.query'



