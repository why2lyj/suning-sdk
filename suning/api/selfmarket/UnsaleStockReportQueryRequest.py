# -*- coding: utf-8 -*-

'''

Created on 2016-3-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnsaleStockReportQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.productCode = None
        self.supplierProductCode = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryUnsaleStockReport'

    def getApiMethod(self):

        return 'suning.unsalestockreport.query'



