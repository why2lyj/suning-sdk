# -*- coding: utf-8 -*-

'''

Created on 2020-5-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundlistinformationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endModified = None
        self.pageNo = None
        self.pageSize = None
        self.returnStatus = None
        self.startModified = None
        
        self.setParamRule({
        	'endModified':{'allow_empty':False},
        	'startModified':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRefundlistinformation'

    def getApiMethod(self):

        return 'suning.custom.refundlistinformation.query'



