# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BookmainproductModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.correctParams = None
        self.itemCode = None
        self.productCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'mainProduct'

    def getApiMethod(self):

        return 'suning.custom.bookmainproduct.modify'



