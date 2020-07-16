# -*- coding: utf-8 -*-

'''

Created on 2014-10-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class QueryFullReductionRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.promotionRange = None
        self.statusCode = None



    def getApiBizName(self):

        return 'queryFullReduction'



    def getApiMethod(self):

        return 'suning.custom.fullreduction.query'



