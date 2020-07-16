# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurchaseOrderReportQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        self.startDate = None
        self.endDate = None
        self.supplierCode = None
        self.orderType = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'startDate':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrderReport'

    def getApiMethod(self):

        return 'suning.purchaseorderreport.query'



