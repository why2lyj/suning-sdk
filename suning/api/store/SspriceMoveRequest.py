# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SspriceMoveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.appStoreCode = None
        self.operationType = None
        self.storeCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'operationType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'moveSsprice'

    def getApiMethod(self):

        return 'suning.store.ssprice.move'



