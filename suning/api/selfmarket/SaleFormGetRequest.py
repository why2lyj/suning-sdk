# -*- coding: utf-8 -*-

'''

Created on 2018-11-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleFormGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.brandCode = None
        self.imei = None
        self.supplierCode = None
        
        self.setParamRule({
        	'brandCode':{'allow_empty':False},
        	'imei':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getSaleform'

    def getApiMethod(self):

        return 'suning.selfmarket.saleform.get'



