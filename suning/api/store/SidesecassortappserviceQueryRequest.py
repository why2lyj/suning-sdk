# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidesecassortappserviceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.protypeid = None
        self.storeCode = None
        
        self.setParamRule({
        	'appStoreCode':{'allow_empty':False},
        	'protypeid':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySidesecassortappservice'

    def getApiMethod(self):

        return 'suning.store.sidesecassortappservice.query'



