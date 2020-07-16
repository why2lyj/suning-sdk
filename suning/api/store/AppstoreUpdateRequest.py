# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class AppstoreUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appStoreCode = None
        self.branchStoreName = None
        self.custNum = None
        self.dayHours = None
        self.latitude = None
        self.longitude = None
        self.openDay = None
        self.storeAdd = None
        self.storeArea = None
        self.storeCode = None
        self.storeCondues = None
        self.storeContact = None
        self.storeDeliveryMode = None
        self.storeInCity = None
        self.storeInProVince = None
        self.storeLogo = None
        self.storeName = None
        self.storePict = None
        self.storeStatus = None
        self.storeTel = None
        
        self.setParamRule({
        	'appStoreCode':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'updateAppstore'

    def getApiMethod(self):

        return 'suning.store.appstore.update'



