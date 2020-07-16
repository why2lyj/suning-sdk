# -*- coding: utf-8 -*-

'''

Created on 2018-1-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyStatus = None
        self.brandCode = None
        self.categoryCode = None
        self.cmTitle = None
        self.contentStatus = None
        self.endTime = None
        self.itemCode = None
        self.pageNo = None
        self.pageSize = None
        self.productCode = None
        self.startTime = None
        self.supplierCodeAsk = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryItem'

    def getApiMethod(self):

        return 'suning.selfmarket.item.query'



