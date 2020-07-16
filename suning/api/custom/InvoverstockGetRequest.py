# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoverstockGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.payeeRegisterNo = None
        self.platformCoding = None
        
        self.setParamRule({
        	'payeeRegisterNo':{'allow_empty':False},
        	'platformCoding':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getInvoverstock'

    def getApiMethod(self):

        return 'suning.custom.invoverstock.get'



