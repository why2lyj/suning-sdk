# -*- coding: utf-8 -*-

'''

Created on 2015-2-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class HistoryorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.userName = None
        self.userID = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'historyOrderQuery'

    def getApiMethod(self):

        return 'suning.custom.historyorder.query'



