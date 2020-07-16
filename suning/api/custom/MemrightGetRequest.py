# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class MemrightGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.memCode = None
        self.rightType = None
        
        self.setParamRule({
        	'memCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getMemright'

    def getApiMethod(self):

        return 'suning.custom.memright.get'



