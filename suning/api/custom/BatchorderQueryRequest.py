# -*- coding: utf-8 -*-

'''

Created on 2018-5-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class BatchorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryBatchorder'

    def getApiMethod(self):

        return 'suning.custom.batchorder.query'



