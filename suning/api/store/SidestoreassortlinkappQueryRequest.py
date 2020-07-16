# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidestoreassortlinkappQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.productCode = None
        self.storeCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySidestoreassortlinkapp'

    def getApiMethod(self):

        return 'suning.store.sidestoreassortlinkapp.query'



