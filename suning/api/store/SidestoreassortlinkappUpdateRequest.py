# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidestoreassortlinkappUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.parentProdCode = None
        self.prodCodeType = None
        self.productCode = None
        self.protypeid = None
        self.storeCode = None
        
        self.setParamRule({
        	'parentProdCode':{'allow_empty':False},
        	'prodCodeType':{'allow_empty':False},
        	'productCode':{'allow_empty':False},
        	'protypeid':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'updateSidestoreassortlinkapp'

    def getApiMethod(self):

        return 'suning.store.sidestoreassortlinkapp.update'



