# -*- coding: utf-8 -*-

'''

Created on 2019-7-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class StorageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.storage = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryStorage'

    def getApiMethod(self):

        return 'suning.custom.storage.query'



