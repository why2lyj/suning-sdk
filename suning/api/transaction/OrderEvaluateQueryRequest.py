# -*- coding: utf-8 -*-

'''

Created on 2016-5-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderEvaluateQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.evaluateLevel = None
        self.startTime = None
        self.endTime = None
        self.isAddComments = None
        self.isReply = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrderEvaluate'

    def getApiMethod(self):

        return 'suning.custom.orderevaluate.query'



