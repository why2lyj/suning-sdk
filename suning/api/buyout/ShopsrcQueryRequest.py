# -*- coding: utf-8 -*-

'''

Created on 2019-10-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopsrcQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.city = None
        self.cmmdtyInfo = None
        self.county = None
        self.province = None
        self.village = None
        
        self.setParamRule({
        	'city':{'allow_empty':False},
        	'county':{'allow_empty':False},
        	'province':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryShopsrc'

    def getApiMethod(self):

        return 'suning.buyout.shopsrc.query'



