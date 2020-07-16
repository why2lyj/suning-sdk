# -*- coding: utf-8 -*-

'''

Created on 2019-3-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductsaleareaQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemCode = None
        self.productCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryProductsalearea'

    def getApiMethod(self):

        return 'suning.custom.productsalearea.query'



