# -*- coding: utf-8 -*-

'''

Created on 2020-4-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnpaidorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.supplierCode = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryUnpaidorder'

    def getApiMethod(self):

        return 'suning.selfmarket.unpaidorder.query'



