# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class QueryPriceReduceRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.timeType = None
        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.acStatusCode = None



    def getApiBizName(self):

        return 'queryPriceReduce'



    def getApiMethod(self):

        return 'suning.custom.pricereduce.query'



