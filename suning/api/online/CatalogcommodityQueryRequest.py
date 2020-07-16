# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class CatalogcommodityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.catalogId = None
        
        self.setParamRule({
        	'catalogId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCatalogcommodity'

    def getApiMethod(self):

        return 'suning.online.catalogcommodity.query'



