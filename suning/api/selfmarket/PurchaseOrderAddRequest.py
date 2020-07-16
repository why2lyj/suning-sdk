# -*- coding: utf-8 -*-

'''

Created on 2018-8-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurchaseOrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.confirmDeliveryDate = None
        self.confirmType = None
        self.itemNo = None
        self.orderCode = None
        self.supplierCode = None
        
        self.setParamRule({
        	'confirmType':{'allow_empty':False},
        	'itemNo':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'purchaseOrderConfirm'

    def getApiMethod(self):

        return 'suning.selfmarket.purchaseorder.add'



