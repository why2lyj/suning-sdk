# -*- coding: utf-8 -*-

'''

Created on 2020-4-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class ComposestrategyCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.description = None
        self.keywords = None
        self.name = None
        self.strategyIdA = None
        self.strategyIdB = None
        
        self.setParamRule({
        	'keywords':{'allow_empty':False},
        	'name':{'allow_empty':False},
        	'strategyIdA':{'allow_empty':False},
        	'strategyIdB':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createComposestrategy'

    def getApiMethod(self):

        return 'suning.custom.composestrategy.create'



