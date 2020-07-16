# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SnreturnorderinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endModified = None
        self.orderNo = None
        self.pageNo = None
        self.pageSize = None
        self.startModified = None
        
        self.setParamRule({
        	'orderNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySnreturnorderinfo'

    def getApiMethod(self):

        return 'suning.store.snreturnorderinfo.query'



