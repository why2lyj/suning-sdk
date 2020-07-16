# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductoperateDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.partnumber = None
        self.custNum = None
        self.shopId = None
        
        self.setParamRule({
        	'partnumber':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'shopId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteProductoperate'

    def getApiMethod(self):

        return 'suning.custom.productoperate.delete'



