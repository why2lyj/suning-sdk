# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class AppstoreQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.custNum = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryAppstore'

    def getApiMethod(self):

        return 'suning.store.appstore.query'



