# -*- coding: utf-8 -*-

'''

Created on 2019-3-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class CapacityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endDate = None
        self.orderCode = None
        self.startDate = None
        self.supplierCode = None
        
        self.setParamRule({
        	'endDate':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCapacity'

    def getApiMethod(self):

        return 'suning.selfmarket.capacity.query'



