# -*- coding: utf-8 -*-

'''

Created on 2015-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class HistoryOrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.serverId = None
        self.chargeId = None
        self.startTime = None
        self.endTime = None
        self.orderCategory = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryHistoryOrder'

    def getApiMethod(self):

        return 'suning.fws.historyorder.query'



