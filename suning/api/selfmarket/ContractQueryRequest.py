# -*- coding: utf-8 -*-

'''

Created on 2015-1-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class ContractQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.isSign = None
        self.supplierCode = None
        self.pageNo = None
        self.pageSize = None



    def getApiBizName(self):

        return 'queryContract'



    def getApiMethod(self):

        return 'suning.selfmarket.contract.query'



