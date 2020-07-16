# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoragesubAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseCode = None
        self.storageDate = None
        self.storageTime = None
        self.carrier = None
        self.contactsNumber = None
        self.waybill = None
        self.purchaseOrderId = None
        self.customerId = None
        self.commodityList = None
        
        self.setParamRule({
        	'warehouseCode':{'allow_empty':False},
        	'storageDate':{'allow_empty':False},
        	'storageTime':{'allow_empty':False},
        	'carrier':{'allow_empty':False},
        	'contactsNumber':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addStoragesub'

    def getApiMethod(self):

        return 'suning.fourps.storagesub.add'



