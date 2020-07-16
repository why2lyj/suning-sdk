# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApprovalResultQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.type = None
        self.applyCode = None
        self.createStartDate = None
        self.createEndDate = None
        self.modelType = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'type':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryApprovalResult'

    def getApiMethod(self):

        return 'suning.approvalresult.query'



