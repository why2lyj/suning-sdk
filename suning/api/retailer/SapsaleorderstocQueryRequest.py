# -*- coding: utf-8 -*-

'''

Created on 2018-9-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class SapsaleorderstocQueryRequest(AbstractApi):

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
        	'appId':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	'merchantCustNo':{'allow_empty':False},
        	'startDate':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySapsaleorderstoc'

    def getApiMethod(self):

        return 'suning.retailer.sapsaleorderstoc.query'



