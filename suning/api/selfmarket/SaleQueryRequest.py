# -*- coding: utf-8 -*-

'''

Created on 2017-12-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.gdsCd = None
        self.pageNo = None
        self.pageSize = None
        self.statisEndDate = None
        self.statisStartDate = None
        self.vendorCd = None
        self.vendorGds = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'statisEndDate':{'allow_empty':False},
        	'statisStartDate':{'allow_empty':False},
        	'vendorCd':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySale'

    def getApiMethod(self):

        return 'suning.selfmarket.sale.query'



