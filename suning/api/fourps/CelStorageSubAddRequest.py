# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class CelStorageSubAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseCode = None
        self.refundType = None
        self.purchaseOrderId = None
        self.customerId = None
        self.appointDate = None
        self.appointTime = None
        self.contacts = None
        self.supplierPhone = None
        self.note = None
        self.commodityList = None
        
        self.setParamRule({
        	'warehouseCode':{'allow_empty':False},
        	'refundType':{'allow_empty':False},
        	'appointDate':{'allow_empty':False},
        	'appointTime':{'allow_empty':False},
        	'contacts':{'allow_empty':False},
        	'supplierPhone':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addCelStorageSub'

    def getApiMethod(self):

        return 'suning.fourps.celstoragesub.add'



