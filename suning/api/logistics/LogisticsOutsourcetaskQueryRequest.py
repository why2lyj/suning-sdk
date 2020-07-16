# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsOutsourcetaskQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.pageSize = None
        self.pageNo = None



    def getApiBizName(self):

        return 'queryLogisticsOutsourceTask'



    def getApiMethod(self):

        return 'suning.logistics.outsourcetask.query'



