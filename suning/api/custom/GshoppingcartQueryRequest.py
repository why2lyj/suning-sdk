# -*- coding: utf-8 -*-

'''

Created on 2020-2-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class GshoppingcartQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.customerNo = None
        self.productCode = None
        
        self.setParamRule({
        	'customerNo':{'allow_empty':False},
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGshoppingcart'

    def getApiMethod(self):

        return 'suning.custom.gshoppingcart.query'



