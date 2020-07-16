# -*- coding: utf-8 -*-

'''

Created on 2017-5-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProdextendGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skus = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getProdextend'

    def getApiMethod(self):

        return 'suning.govbus.prodextend.get'



