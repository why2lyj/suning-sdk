# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class StorageSubQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.orderState = None
        self.warehouseCode = None
        self.orderBeginDate = None
        self.orderEndDate = None
        self.applyBeginDate = None
        self.applyEndDate = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryStorageSub'

    def getApiMethod(self):

        return 'suning.fourps.storagesub.query'



