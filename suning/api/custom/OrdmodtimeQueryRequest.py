# -*- coding: utf-8 -*-

'''

Created on 2019-4-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdmodtimeQueryRequest(AbstractApi):

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
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'orderQuery'

    def getApiMethod(self):

        return 'suning.custom.ordmodtime.query'



