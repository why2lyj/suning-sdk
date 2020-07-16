# -*- coding: utf-8 -*-

'''

Created on 2017-7-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleorderpromotioninfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySaleorderpromotioninfo'

    def getApiMethod(self):

        return 'suning.selfmarket.saleorderpromotioninfo.query'



