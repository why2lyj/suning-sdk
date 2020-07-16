# -*- coding: utf-8 -*-

'''

Created on 2019-4-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurweekplanQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.purchaseWeekPlanNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	'purchaseWeekPlanNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPurweekplan'

    def getApiMethod(self):

        return 'suning.selfmarket.purweekplan.query'



