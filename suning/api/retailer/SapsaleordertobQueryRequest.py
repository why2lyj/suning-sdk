# -*- coding: utf-8 -*-

'''

Created on 2018-11-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class SapsaleordertobQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.endDate = None
        self.merchantCustNo = None
        self.startDate = None
        self.storeCode = None
        
        self.setParamRule({
        	'endDate':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySapsaleordertob'

    def getApiMethod(self):

        return 'suning.retailer.sapsaleorderstob.query'



