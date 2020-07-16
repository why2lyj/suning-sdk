# -*- coding: utf-8 -*-

'''

Created on 2019-12-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductoperateConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.partnumber = None
        self.shopId = None
        self.custNum = None
        
        self.setParamRule({
        	'partnumber':{'allow_empty':False},
        	'shopId':{'allow_empty':False},
        	'custNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmProductoperate'

    def getApiMethod(self):

        return 'suning.custom.productoperate.confirm'



