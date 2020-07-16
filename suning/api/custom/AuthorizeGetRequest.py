# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class AuthorizeGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.name = None
        self.redirectUrl = None
        self.timeStamp = None
        self.userId = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'name':{'allow_empty':False},
        	'redirectUrl':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False},
        	'userId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getAuthorize'

    def getApiMethod(self):

        return 'suning.custom.authorize.get'



