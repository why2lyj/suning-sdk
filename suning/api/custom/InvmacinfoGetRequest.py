# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvmacinfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.extensionNumber = None
        self.payeeRegisterNo = None
        self.platformCoding = None
        self.taxClearState = None
        self.taxCopyState = None
        
        self.setParamRule({
        	'payeeRegisterNo':{'allow_empty':False},
        	'platformCoding':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getInvmacinfo'

    def getApiMethod(self):

        return 'suning.custom.invmacinfo.get'



