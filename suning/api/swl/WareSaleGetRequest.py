# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class WareSaleGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseType = None
        self.warehouseCode = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getWareSale'

    def getApiMethod(self):

        return 'suning.swl.waresale.get'



