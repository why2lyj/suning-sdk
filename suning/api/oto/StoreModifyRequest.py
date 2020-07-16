# -*- coding: utf-8 -*-

'''

Created on 2018-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoreModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.branchStoreName = None
        self.dayHours = None
        self.latitude = None
        self.longitude = None
        self.ownstoreCode = None
        self.storeAdd = None
        self.storeArea = None
        self.storeCode = None
        self.storeCondues = None
        self.storeName = None
        self.storeInProVince = None
        self.storeInCity = None
        self.storeTel = None
        self.storeStatus = None
        self.storePict = None
        self.storeEpp = None
        self.storeEppPayFlag = None
        self.storeEppPay = None
        self.storeSend = None
        
        self.setParamRule({
        	'dayHours':{'allow_empty':False},
        	'latitude':{'allow_empty':False},
        	'longitude':{'allow_empty':False},
        	'storeAdd':{'allow_empty':False},
        	'storeArea':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'storeName':{'allow_empty':False},
        	'storeInProVince':{'allow_empty':False},
        	'storeInCity':{'allow_empty':False},
        	'storeTel':{'allow_empty':False},
        	'storeStatus':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyStore'

    def getApiMethod(self):

        return 'suning.oto.store.modify'



