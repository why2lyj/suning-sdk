# -*- coding: utf-8 -*-

'''

Created on 2019-10-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.receiveRefundList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'receiveRefund'

    def getApiMethod(self):

        return 'suning.customjlf.refund.receive'



