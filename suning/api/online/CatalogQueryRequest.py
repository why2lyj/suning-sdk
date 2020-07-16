# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class CatalogQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.catalogId = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryCatalog'

    def getApiMethod(self):

        return 'suning.online.catalog.query'



