# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class SalesstatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.physicalCode = None
        self.salesStatus = None
        self.productName = None
        self.categoryCode = None
        self.itemCode = None
        self.productCode = None
        self.brandCode = None
        
        self.setParamRule({
        	'physicalCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySalesstatus'

    def getApiMethod(self):

        return 'suning.oto.salesstatus.query'



