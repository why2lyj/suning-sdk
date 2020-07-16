# -*- coding: utf-8 -*-

'''

Created on 2016-6-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class StatementGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.guid = None
        self.zcjsqdm = None
        self.zawbs = None
        self.zkpje = None
        self.noteHeader = None
        self.factoryBp = None
        self.detail = None
        
        self.setParamRule({
        	'guid':{'allow_empty':False},
        	'zcjsqdm':{'allow_empty':False},
        	'zawbs':{'allow_empty':False},
        	'zkpje':{'allow_empty':False},
        	'factoryBp':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getStatement'

    def getApiMethod(self):

        return 'suning.asmp.statement.get'



