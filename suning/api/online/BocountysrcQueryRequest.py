# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class BocountysrcQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

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

        return 'queryBocountysrc'

    def getApiMethod(self):

        return 'suning.online.bocountysrc.query'



