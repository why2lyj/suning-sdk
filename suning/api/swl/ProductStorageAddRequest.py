# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductStorageAddRequest(AbstractApi):

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
        self.commoditys = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addProductStorage'

    def getApiMethod(self):

        return 'suning.swl.productstorage.add'



