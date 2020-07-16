# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class CustCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.authType = None
        self.filesContents = None
        self.filesSuffix = None
        self.timeStamp = None
        self.userId = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'authType':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False},
        	'userId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createCust'

    def getApiMethod(self):

        return 'suning.custom.cust.create'



