# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurmonthplanQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.purchaseMonthPlanNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	'purchaseMonthPlanNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPurmonthplan'

    def getApiMethod(self):

        return 'suning.selfmarket.purmonthplan.query'



