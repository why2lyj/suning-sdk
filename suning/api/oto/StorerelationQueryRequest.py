# -*- coding: utf-8 -*-

'''

Created on 2018-10-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class StorerelationQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.groupCode = None
        self.supplierCode = None
        
        self.setParamRule({
        	'groupCode':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryStorerelation'

    def getApiMethod(self):

        return 'suning.oto.storerelation.query'



