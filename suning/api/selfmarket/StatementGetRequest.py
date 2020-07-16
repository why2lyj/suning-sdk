# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class StatementGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.confirmHead = None
        self.confirmDetail = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmStatement'

    def getApiMethod(self):

        return 'suning.statement.confirm'



