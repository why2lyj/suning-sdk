# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderdiscountQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.activityStatus = None
        self.appStoreCode = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.storeCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryOrderdiscount'

    def getApiMethod(self):

        return 'suning.store.orderdiscount.query'



