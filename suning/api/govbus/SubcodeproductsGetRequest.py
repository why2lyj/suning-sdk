# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class SubcodeproductsGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.generalSku = None
        
        self.setParamRule({
        	'generalSku':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getSubcodeproducts'

    def getApiMethod(self):

        return 'suning.govbus.subcodeproducts.get'



