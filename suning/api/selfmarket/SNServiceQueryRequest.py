# -*- coding: utf-8 -*-

'''

Created on 2016-4-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class SNServiceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.recordGuId = None
        self.itemGuId = None
        self.srvOrdId = None
        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'snserviceget'

    def getApiMethod(self):

        return 'suning.snservice.get'



