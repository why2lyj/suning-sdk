# -*- coding: utf-8 -*-

'''

Created on 2017-7-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class ServiceinformationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderStatus = None
        self.startTime = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'orderStatus':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryServiceinformation'

    def getApiMethod(self):

        return 'suning.fontorder.serviceinformation.query'



