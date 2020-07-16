# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SidestoreassortappserviceUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.operateType = None
        self.parentid = None
        self.protypeid = None
        self.ptname = None
        self.storeCode = None
        
        self.setParamRule({
        	'operateType':{'allow_empty':False},
        	'parentid':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'updateSidestoreassortappservice'

    def getApiMethod(self):

        return 'suning.store.sidestoreassortappservice.update'



