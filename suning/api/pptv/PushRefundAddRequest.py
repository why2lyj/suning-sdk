# -*- coding: utf-8 -*-

'''

Created on 2017-4-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class PushRefundAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.buyerNick = None
        self.companyName = None
        self.createdTime = None
        self.desc = None
        self.modifiedTime = None
        self.num = None
        self.oid = None
        self.orderStatus = None
        self.outerId = None
        self.reason = None
        self.refundFee = None
        self.refundId = None
        self.refundNum = None
        self.refundPhase = None
        self.refundVersion = None
        self.sellerNick = None
        self.sid = None
        self.status = None
        self.tid = None
        self.title = None
        self.totalFee = None
        self.type = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addPushRefund'

    def getApiMethod(self):

        return 'suning.pptv.pushrefund.add'



