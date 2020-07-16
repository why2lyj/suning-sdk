# -*- coding: utf-8 -*-

'''

Created on 2017-4-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class SnserviceGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.itemGuId = None
        self.pageNo = None
        self.pageSize = None
        self.recordGuId = None
        self.srvOrdId = None
        self.startTime = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'snserviceget'

    def getApiMethod(self):

        return 'suning.selfmarket.snservice.get'



