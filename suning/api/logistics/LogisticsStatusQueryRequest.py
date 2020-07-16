# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsStatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.pageSize = None
        self.pageNo = None
        self.operationStatus = None



    def getApiBizName(self):

        return 'queryLogisticStatus'



    def getApiMethod(self):

        return 'suning.custom.logisticsstatus.query'



