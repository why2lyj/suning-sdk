# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoreQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.storeCode = None
        
        self.setParamRule({
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryStore'

    def getApiMethod(self):

        return 'suning.oto.store.query'



