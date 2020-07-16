# -*- coding: utf-8 -*-

'''

Created on 2015-2-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnpaidorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.orderLineStatus = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'unpaidOrder'

    def getApiMethod(self):

        return 'suning.custom.unpaidorder.query'



