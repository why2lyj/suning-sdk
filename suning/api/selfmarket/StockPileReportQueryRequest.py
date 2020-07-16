# -*- coding: utf-8 -*-

'''

Created on 2016-3-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class StockPileReportQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.category = None
        self.supplierCode = None
        self.productCode = None
        self.supplierProductCode = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'category':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryStockReport'

    def getApiMethod(self):

        return 'suning.stockreport.query'



