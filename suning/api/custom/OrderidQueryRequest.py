# -*- coding: utf-8 -*-

'''

Created on 2017-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderidQueryRequest(AbstractApi):

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
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrderid'

    def getApiMethod(self):

        return 'suning.custom.orderid.query'



