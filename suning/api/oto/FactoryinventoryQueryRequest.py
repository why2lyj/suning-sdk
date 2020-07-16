# -*- coding: utf-8 -*-

'''

Created on 2018-1-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class FactoryinventoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseCode = None
        self.commodityCodes = None
        self.supplierCommoditys = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'warehouseCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryFactoryinventory'

    def getApiMethod(self):

        return 'suning.oto.factoryinventory.query'



