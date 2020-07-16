# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SalesstatusUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.storeCode = None
        self.appStoreCode = None
        self.dataList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'updateSalesstatus'

    def getApiMethod(self):

        return 'suning.store.salesstatus.update'



