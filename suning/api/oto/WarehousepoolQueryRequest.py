# -*- coding: utf-8 -*-

'''

Created on 2017-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class WarehousepoolQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.warehouseCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryWarehousepool'

    def getApiMethod(self):

        return 'suning.oto.warehousepool.query'



