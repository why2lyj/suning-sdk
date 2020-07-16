# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class LeaderorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderLineStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'orderLineStatus':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryLeaderorder'

    def getApiMethod(self):

        return 'suning.netalliance.leaderorder.query'



