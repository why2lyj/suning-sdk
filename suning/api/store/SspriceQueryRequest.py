# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SspriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.activityStatus = None
        self.appStoreCode = None
        self.pageNo = None
        self.pageSize = None
        self.storeCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'querySsprice'

    def getApiMethod(self):

        return 'suning.store.ssprice.query'



