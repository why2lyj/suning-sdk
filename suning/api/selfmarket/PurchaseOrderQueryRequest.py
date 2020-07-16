# -*- coding: utf-8 -*-

'''

Created on 2017-6-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurchaseOrderQueryRequest(AbstractApi):

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
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'purchaseOrder'

    def getApiMethod(self):

        return 'suning.selfmarket.purchaseorder.query'



