# -*- coding: utf-8 -*-

'''

Created on 2016-12-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class FactorygoodsinvQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.goodsList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryFactorygoodsinv'

    def getApiMethod(self):

        return 'suning.selfmarket.factorygoodsinv.query'



