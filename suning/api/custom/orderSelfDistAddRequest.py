# -*- coding: utf-8 -*-

'''

Created on 2018-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class orderSelfDistAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deliveryPerName = None
        self.deliveryPerPhone = None
        self.deliveryTime = None
        self.orderCode = None
        self.orderLineNumbers = None
        self.phoneIdentifyCodes = None
        self.productCodes = None
        
        self.setParamRule({
        	'deliveryPerName':{'allow_empty':False},
        	'deliveryPerPhone':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'orderSelfDist'

    def getApiMethod(self):

        return 'suning.custom.orderselfdist.add'



