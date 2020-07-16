# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class SspriceCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityChannel = None
        self.activityCode = None
        self.activityName = None
        self.appStoreCode = None
        self.endTime = None
        self.operationType = None
        self.priceType = None
        self.productList = None
        self.startTime = None
        self.storeCode = None
        
        self.setParamRule({
        	'activityChannel':{'allow_empty':False},
        	'operationType':{'allow_empty':False},
        	'priceType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createSsprice'

    def getApiMethod(self):

        return 'suning.store.ssprice.create'



