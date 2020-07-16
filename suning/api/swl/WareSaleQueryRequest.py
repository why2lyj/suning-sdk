# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class WareSaleQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseType = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryWareSale'

    def getApiMethod(self):

        return 'suning.swl.waresale.query'



