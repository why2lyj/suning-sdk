# -*- coding: utf-8 -*-

'''

Created on 2019-6-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class RejectedQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.beginTime = None
        self.dealStatus = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.supplierCode = None
        
        self.setParamRule({
        	'beginTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryRejected'

    def getApiMethod(self):

        return 'suning.selfmarket.rejected.query'



