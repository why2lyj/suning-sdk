# -*- coding: utf-8 -*-

'''

Created on 2018-10-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class verificationInfoModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.eleCode = None
        self.codeType = None
        self.storeCode = None
        self.storeName = None
        
        self.setParamRule({
        	'eleCode':{'allow_empty':False},
        	'codeType':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	'storeName':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'verificationInfo'

    def getApiMethod(self):

        return 'suning.custom.code.modify'



