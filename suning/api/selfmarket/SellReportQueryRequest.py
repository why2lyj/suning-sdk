# -*- coding: utf-8 -*-

'''

Created on 2016-3-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class SellReportQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.createTimeStart = None
        self.createTimeEnd = None
        self.supplierCode = None
        self.productCode = None
        self.supplierProductCode = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'createTimeStart':{'allow_empty':False},
        	'createTimeEnd':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySalesReport'

    def getApiMethod(self):

        return 'suning.salesreport.query'



