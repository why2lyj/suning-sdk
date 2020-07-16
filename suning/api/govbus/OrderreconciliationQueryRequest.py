# -*- coding: utf-8 -*-

'''

Created on 2020-1-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderreconciliationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.dateType = None
        self.endDate = None
        self.orderItemStatus = None
        self.pageNo = None
        self.pageSize = None
        self.queryType = None
        self.startDate = None
        self.sysCode = None
        self.uid = None
        
        self.setParamRule({
        	'dateType':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'sysCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrderreconciliation'

    def getApiMethod(self):

        return 'suning.govbus.orderreconciliation.query'



