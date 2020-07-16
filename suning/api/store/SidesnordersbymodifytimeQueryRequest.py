# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesnordersbymodifytimeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.endTime = None
        self.orderStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.storeCode = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySidesnordersbymodifytime'

    def getApiMethod(self):

        return 'suning.store.sidesnordersbymodifytime.query'



