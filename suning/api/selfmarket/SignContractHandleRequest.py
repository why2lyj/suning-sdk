# -*- coding: utf-8 -*-

'''

Created on 2015-1-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class SignContractHandleRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.contractCode = None
        self.supplierCode = None
        self.contractText = None
        self.signText = None



    def getApiBizName(self):

        return 'handleSignContract'



    def getApiMethod(self):

        return 'suning.selfmarket.signcontract.handle'



