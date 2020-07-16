# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class SignBindStatementRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.signHead = None
        self.signDetail = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'signBindStatement'

    def getApiMethod(self):

        return 'suning.bindstatement.sign'



