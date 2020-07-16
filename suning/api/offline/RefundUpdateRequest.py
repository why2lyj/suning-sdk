# -*- coding: utf-8 -*-

'''

Created on 2018-10-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemId = None
        self.operateFlag = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False},
        	'operateFlag':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateRefund'

    def getApiMethod(self):

        return 'suning.offline.refund.update'



