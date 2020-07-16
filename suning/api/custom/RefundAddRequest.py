# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.amount = None
        self.fixedEndTime = None
        self.fixedStartTime = None
        self.holidayEndTime = None
        self.holidayStartTime = None
        self.payTime = None
        self.refundTime = None
        self.tabNumber = None
        
        self.setParamRule({
        	'tabNumber':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addRefund'

    def getApiMethod(self):

        return 'suning.custom.refund.add'



