# -*- coding: utf-8 -*-

'''

Created on 2018-9-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleorderstocQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.merchantCustNo = None
        self.storeCode = None
        self.startDate = None
        self.endDate = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'endDate':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySaleorderstoc'

    def getApiMethod(self):

        return 'suning.retailer.saleorderstoc.query'



