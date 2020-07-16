# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydcmmdtyfreightQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.city = None
        self.county = None
        self.paymentType = None
        self.provinc = None
        self.sku = None
        self.token = None
        self.town = None
        
        self.setParamRule({
        	'city':{'allow_empty':False},
        	'county':{'allow_empty':False},
        	'paymentType':{'allow_empty':False},
        	'provinc':{'allow_empty':False},
        	'token':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryJsydcmmdtyfreight'

    def getApiMethod(self):

        return 'suning.retailer.jsydcmmdtyfreight.query'



