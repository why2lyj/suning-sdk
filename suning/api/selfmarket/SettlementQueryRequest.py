# -*- coding: utf-8 -*-

'''

Created on 2018-11-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class SettlementQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endDate = None
        self.pageNo = None
        self.pageSize = None
        self.startDate = None
        self.supplierCode = None
        
        self.setParamRule({
        	'endDate':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySettlement'

    def getApiMethod(self):

        return 'suning.selfmarket.settlement.query'



