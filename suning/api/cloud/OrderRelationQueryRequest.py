# -*- coding: utf-8 -*-

'''

Created on 2015-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderRelationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.appId = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrderRelation'

    def getApiMethod(self):

        return 'suning.cloud.orderrelation.query'



