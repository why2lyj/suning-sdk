# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class CelStorageSubQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.appointStatus = None
        self.refundType = None
        self.warehouseCode = None
        self.appointStartTime = None
        self.appointEndTime = None
        self.startTime = None
        self.endTime = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryCelStorageSub'

    def getApiMethod(self):

        return 'suning.fourps.celstoragesub.query'



