# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderevalQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.reviewLevel = None
        self.suplReviewFlag = None
        self.replyOrNot = None
        self.pageNo = None
        self.pageSize = None



    def getApiBizName(self):

        return 'queryOrderEval'



    def getApiMethod(self):

        return 'suning.custom.ordereval.query'



