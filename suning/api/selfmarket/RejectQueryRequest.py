# -*- coding: utf-8 -*-

'''

Created on 2018-12-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class RejectQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.gdsCd = None
        self.pageNo = None
        self.pageSize = None
        self.vendorCd = None
        self.vendorGds = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'vendorCd':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryReject'

    def getApiMethod(self):

        return 'suning.selfmarket.reject.query'



