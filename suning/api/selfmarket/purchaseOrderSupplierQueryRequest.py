# -*- coding: utf-8 -*-

'''

Created on 2019-4-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class purchaseOrderSupplierQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endDate = None
        self.orderCode = None
        self.orderStatus = None
        self.orderType = None
        self.pageNo = None
        self.pageSize = None
        self.startDate = None
        self.supplierCode = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'purchaseOrder'

    def getApiMethod(self):

        return 'suning.selfmarket.purchaseordersupplier.query'



