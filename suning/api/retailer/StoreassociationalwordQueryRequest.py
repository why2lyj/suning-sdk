# -*- coding: utf-8 -*-

'''

Created on 2020-3-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoreassociationalwordQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.keyword = None
        self.pnumber = None
        self.psize = None
        self.storeCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryStoreassociationalword'

    def getApiMethod(self):

        return 'suning.retailer.storeassociationalword.query'



