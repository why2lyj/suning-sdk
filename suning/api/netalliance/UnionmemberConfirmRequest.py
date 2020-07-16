# -*- coding: utf-8 -*-

'''

Created on 2020-3-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnionmemberConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        self.mixCustNum = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmUnionmember'

    def getApiMethod(self):

        return 'suning.netalliance.unionmember.confirm'



