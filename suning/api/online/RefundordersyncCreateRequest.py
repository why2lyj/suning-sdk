# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundordersyncCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.createDate = None
        self.orderId = None
        self.orderItemId = None
        self.payChannelReNumber = None
        self.payNumber = None
        self.refundAmount = None
        self.refundDate = None
        self.refundId = None
        self.refundStatus = None
        self.refundType = None
        
        self.setParamRule({
        	'createDate':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'refundAmount':{'allow_empty':False},
        	'refundDate':{'allow_empty':False},
        	'refundId':{'allow_empty':False},
        	'refundStatus':{'allow_empty':False},
        	'refundType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createRefundordersync'

    def getApiMethod(self):

        return 'suning.online.refundordersync.create'



