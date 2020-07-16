# -*- coding: utf-8 -*-

'''

Created on 2018-10-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemId = None
        self.verifyCode = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False},
        	'verifyCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmRefund'

    def getApiMethod(self):

        return 'suning.offline.refund.confirm'



