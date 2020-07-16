# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvbalanceGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.payeeRegisterNo = None
        self.platformCoding = None
        self.queryType = None
        
        self.setParamRule({
        	'payeeRegisterNo':{'allow_empty':False},
        	'platformCoding':{'allow_empty':False},
        	'queryType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getInvbalance'

    def getApiMethod(self):

        return 'suning.custom.invbalance.get'



