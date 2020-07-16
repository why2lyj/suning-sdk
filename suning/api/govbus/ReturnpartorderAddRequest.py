# -*- coding: utf-8 -*-

'''

Created on 2020-4-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReturnpartorderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.aftersaleAddress = None
        self.aftersaleName = None
        self.aftersalePhone = None
        self.bankName = None
        self.cardNumber = None
        self.cardUsername = None
        self.orderId = None
        self.skus = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addReturnpartorder'

    def getApiMethod(self):

        return 'suning.govbus.returnpartorder.add'



