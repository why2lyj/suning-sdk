# -*- coding: utf-8 -*-

'''

Created on 2020-4-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class StrategyDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.strategyId = None
        
        self.setParamRule({
        	'strategyId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteStrategy'

    def getApiMethod(self):

        return 'suning.custom.strategy.delete'



