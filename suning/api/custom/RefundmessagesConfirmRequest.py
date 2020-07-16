# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundmessagesConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.msgImage = None
        self.msgInfo = None
        self.returnApplyId = None
        
        self.setParamRule({
        	'msgInfo':{'allow_empty':False},
        	'returnApplyId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmRefundmessages'

    def getApiMethod(self):

        return 'suning.custom.refundmessages.confirm'



