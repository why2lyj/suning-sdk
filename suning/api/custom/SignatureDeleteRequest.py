# -*- coding: utf-8 -*-

'''

Created on 2020-5-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class SignatureDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.name = None
        self.timeStamp = None
        self.userId = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'name':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'deleteSignature'

    def getApiMethod(self):

        return 'suning.custom.signature.delete'



