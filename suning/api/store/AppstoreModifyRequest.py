# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class AppstoreModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.status = None
        
        self.setParamRule({
        	'appStoreCode':{'allow_empty':False},
        	'status':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyAppstore'

    def getApiMethod(self):

        return 'suning.store.appstore.modify'



