# -*- coding: utf-8 -*-

'''

Created on 2017-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class PaymentwayGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityCode = None
        self.districtCode = None
        self.payAmount = None
        self.provinceCode = None
        self.skuId = None
        self.townCode = None
        
        self.setParamRule({
        	'cityCode':{'allow_empty':False},
        	'districtCode':{'allow_empty':False},
        	'payAmount':{'allow_empty':False},
        	'provinceCode':{'allow_empty':False},
        	'skuId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getPaymentway'

    def getApiMethod(self):

        return 'suning.govbus.paymentway.get'



