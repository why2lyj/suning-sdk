# -*- coding: utf-8 -*-

'''

Created on 2019-11-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class RiskmanagementorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRiskmanagementorder'

    def getApiMethod(self):

        return 'suning.netalliance.riskmanagementorder.query'



