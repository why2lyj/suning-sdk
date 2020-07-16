# -*- coding: utf-8 -*-

'''

Created on 2017-12-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class CodeGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.items = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getCode'

    def getApiMethod(self):

        return 'suning.custom.code.get'



