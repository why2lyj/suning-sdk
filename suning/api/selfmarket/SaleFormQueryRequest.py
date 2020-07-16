# -*- coding: utf-8 -*-

'''

Created on 2018-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleFormQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.brandCode = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.supplierCode = None
        
        self.setParamRule({
        	'brandCode':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySaleForm'

    def getApiMethod(self):

        return 'suning.selfmarket.saleform.query'



