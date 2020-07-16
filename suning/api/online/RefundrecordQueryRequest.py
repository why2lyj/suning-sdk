# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundrecordQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemId = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRefundrecord'

    def getApiMethod(self):

        return 'suning.online.refundrecord.query'



