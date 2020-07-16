# -*- coding: utf-8 -*-

'''

Created on 2020-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class StorehistoricalwordsGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.storeCode = None
        self.userCode = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'userCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getStorehistoricalwords'

    def getApiMethod(self):

        return 'suning.retailer.storehistoricalwords.get'



