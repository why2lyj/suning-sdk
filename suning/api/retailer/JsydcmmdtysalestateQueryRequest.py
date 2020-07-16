# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydcmmdtysalestateQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.city = None
        self.county = None
        self.province = None
        self.skuIds = None
        self.token = None
        self.town = None
        
        self.setParamRule({
        	'city':{'allow_empty':False},
        	'county':{'allow_empty':False},
        	'province':{'allow_empty':False},
        	'skuIds':{'allow_empty':False},
        	'token':{'allow_empty':False},
        	'town':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryJsydcmmdtysalestate'

    def getApiMethod(self):

        return 'suning.retailer.jsydcmmdtysalestate.query'



