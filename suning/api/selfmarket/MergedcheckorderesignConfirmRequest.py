# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class MergedcheckorderesignConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.head = None
        self.checkOrderList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmMergedcheckorderesign'

    def getApiMethod(self):

        return 'suning.selfmarket.mergedcheckorderesign.confirm'



