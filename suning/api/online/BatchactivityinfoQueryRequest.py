# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class BatchactivityinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chanId = None
        self.pageNum = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'pageNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryBatchactivityinfo'

    def getApiMethod(self):

        return 'suning.online.batchactivityinfo.query'



