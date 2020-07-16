# -*- coding: utf-8 -*-

'''

Created on 2020-4-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class LabelstrategyCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.description = None
        self.name = None
        self.strategy = None
        
        self.setParamRule({
        	'name':{'allow_empty':False},
        	'strategy':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createLabelstrategy'

    def getApiMethod(self):

        return 'suning.custom.labelstrategy.create'



