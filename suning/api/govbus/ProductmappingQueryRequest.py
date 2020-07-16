# -*- coding: utf-8 -*-

'''

Created on 2017-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductmappingQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.currentPage = None
        
        self.setParamRule({
        	'currentPage':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryProductmapping'

    def getApiMethod(self):

        return 'suning.govbus.productmapping.query'



