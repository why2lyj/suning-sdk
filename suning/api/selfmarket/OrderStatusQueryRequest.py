# -*- coding: utf-8 -*-

'''

Created on 2015-11-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderStatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderSource = None
        self.startTime = None
        self.endTime = None
        self.queryType = None
        self.pageSize = None
        self.pageNo = None
        
        self.setParamRule({
        	'orderSource':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'queryType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrderStatus'

    def getApiMethod(self):

        return 'suning.fourps.orderstatus.query'



