# -*- coding: utf-8 -*-

'''

Created on 2019-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class SigninvoiceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.parameter = None
        self.confirmType = None
        
        self.setParamRule({
        	'parameter':{'allow_empty':False},
        	'confirmType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySigninvoice'

    def getApiMethod(self):

        return 'suning.govbus.signinvoice.query'



