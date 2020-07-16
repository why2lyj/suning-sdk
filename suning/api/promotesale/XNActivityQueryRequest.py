# -*- coding: utf-8 -*-

'''

Created on 2015-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class XNActivityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.activityStatus = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryXNActivity'

    def getApiMethod(self):

        return 'suning.custom.xnactivity.query'



