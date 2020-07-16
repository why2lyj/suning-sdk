# -*- coding: utf-8 -*-

'''

Created on 2020-2-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProdimageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuId = None
        self.supplierCode = None
        
        self.setParamRule({
        	'skuId':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryProdimage'

    def getApiMethod(self):

        return 'suning.sngoods.prodimage.query'



