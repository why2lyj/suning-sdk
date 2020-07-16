# -*- coding: utf-8 -*-

'''

Created on 2020-4-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderLineStatus = None
        self.pageNo = None
        self.pageSize = None
        self.promotion = None
        self.startTime = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrder'

    def getApiMethod(self):

        return 'suning.netalliance.order.query'



