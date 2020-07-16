# -*- coding: utf-8 -*-

'''

Created on 2016-5-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class HisOrderEvaluateQueryRequest(AbstractApi):

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

        return 'queryHisOrderEvaluate'

    def getApiMethod(self):

        return 'suning.custom.hisorderevaluate.query'



