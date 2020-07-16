# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundstatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemId = None
        self.reOrderItemId = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False},
        	'reOrderItemId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRefundstatus'

    def getApiMethod(self):

        return 'suning.online.refundstatus.query'



