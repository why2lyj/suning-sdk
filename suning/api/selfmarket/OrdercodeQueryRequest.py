# -*- coding: utf-8 -*-

'''

Created on 2017-2-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdercodeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.supplierCode = None
        self.orderStatus = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrdercode'

    def getApiMethod(self):

        return 'suning.selfmarket.ordercode.query'



