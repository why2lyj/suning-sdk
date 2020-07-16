# -*- coding: utf-8 -*-

'''

Created on 2019-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class QuerysingleexchangegoodsGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.omsOrderItemNo = None
        self.supplierCode = None
        self.workordernum = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getQuerysingleexchangegoods'

    def getApiMethod(self):

        return 'suning.selfmarket.querysingleexchangegoods.get'



