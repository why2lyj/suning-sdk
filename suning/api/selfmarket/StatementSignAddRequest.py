# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class StatementSignAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.statementCode = None
        self.snArea = None
        self.snCompany = None
        self.html = None
        self.signature = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	'statementCode':{'allow_empty':False},
        	'snCompany':{'allow_empty':False},
        	'html':{'allow_empty':False},
        	'signature':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'signStatement'

    def getApiMethod(self):

        return 'suning.statement.sign'



