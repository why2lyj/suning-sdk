# -*- coding: utf-8 -*-

'''

Created on 2015-1-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class QueryLogisticsCrossbuyTaskRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.businessType = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryLogisticsCrossbuyTask'

    def getApiMethod(self):

        return 'suning.logistics.crossbuytask.query'



