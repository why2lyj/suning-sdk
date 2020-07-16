# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class ScopeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.pageNo = None
        self.pageSize = None
        self.storeCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryScope'

    def getApiMethod(self):

        return 'suning.store.scope.query'



