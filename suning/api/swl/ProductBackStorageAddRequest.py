# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProductBackStorageAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.warehouseCode = None
        self.refundType = None
        self.appointDate = None
        self.appointTime = None
        self.contacts = None
        self.supplierPhone = None
        self.commodityList = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addProductBackStorage'

    def getApiMethod(self):

        return 'suning.swl.productbackstorage.add'



