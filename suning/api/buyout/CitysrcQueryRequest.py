# -*- coding: utf-8 -*-

'''

Created on 2019-10-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class CitysrcQueryRequest(AbstractApi):

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

        return 'queryCitysrc'

    def getApiMethod(self):

        return 'suning.buyout.citysrc.query'



