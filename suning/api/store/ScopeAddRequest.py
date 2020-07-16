# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class ScopeAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.coverageType = None
        self.deleteFlag = None
        self.latitudeRectangle = None
        self.radius = None
        self.storeCode = None
        
        self.setParamRule({
        	'coverageType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addScope'

    def getApiMethod(self):

        return 'suning.store.scope.add'



