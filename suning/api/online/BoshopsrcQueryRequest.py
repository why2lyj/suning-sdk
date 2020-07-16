# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class BoshopsrcQueryRequest(AbstractApi):

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
        self.businessType = None
        
        self.setParamRule({
        	'city':{'allow_empty':False},
        	'county':{'allow_empty':False},
        	'province':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryBoshopsrc'

    def getApiMethod(self):

        return 'suning.online.boshopsrc.query'



