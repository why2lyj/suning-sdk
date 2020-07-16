# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceforcartQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.chanId = None
        self.city = None
        self.cmmdtyInfo = None
        self.county = None
        self.province = None
        self.village = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'county':{'allow_empty':False},
        	'province':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryPriceforcart'

    def getApiMethod(self):

        return 'suning.online.priceforcart.query'



