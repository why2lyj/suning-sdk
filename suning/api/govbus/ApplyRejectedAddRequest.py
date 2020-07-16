# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApplyRejectedAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.bankName = None
        self.cardNumber = None
        self.cardUsername = None
        self.orderId = None
        self.skus = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addApplyRejected'

    def getApiMethod(self):

        return 'suning.govbus.applyrejected.add'



