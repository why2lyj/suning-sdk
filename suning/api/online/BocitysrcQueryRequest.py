# -*- coding: utf-8 -*-

'''

Created on 2020-1-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class BocitysrcQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.city = None
        self.cmmdtyInfo = None
        self.province = None
        
        self.setParamRule({
        	'city':{'allow_empty':False},
        	'province':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryBocitysrc'

    def getApiMethod(self):

        return 'suning.online.bocitysrc.query'



