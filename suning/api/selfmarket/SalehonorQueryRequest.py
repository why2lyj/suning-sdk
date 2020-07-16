# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class SalehonorQueryRequest(AbstractApi):

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
        	'startTime':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySalehonor'

    def getApiMethod(self):

        return 'suning.selfmarket.salehonor.query'



