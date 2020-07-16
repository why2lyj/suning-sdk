# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromAccountBalanceGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getPromAccountBalance'

    def getApiMethod(self):

        return 'suning.advertise.promaccountbalance.get'



