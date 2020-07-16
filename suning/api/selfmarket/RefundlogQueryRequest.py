# -*- coding: utf-8 -*-

'''

Created on 2017-10-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundlogQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.omsItemOrderNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	'omsItemOrderNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRefundlog'

    def getApiMethod(self):

        return 'suning.selfmarket.refundlog.query'



