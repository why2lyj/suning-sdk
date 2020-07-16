# -*- coding: utf-8 -*-

'''

Created on 2019-7-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class FactorygoodsinvModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.goodsList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'modifyFactorygoodsinv'

    def getApiMethod(self):

        return 'suning.selfmarket.factorygoodsinv.modify'



