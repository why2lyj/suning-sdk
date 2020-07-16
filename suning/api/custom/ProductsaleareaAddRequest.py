# -*- coding: utf-8 -*-

'''

Created on 2019-3-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductsaleareaAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.ciyCode = None
        self.itemCode = None
        self.productCode = None
        self.provCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addProductsalearea'

    def getApiMethod(self):

        return 'suning.custom.productsalearea.add'



