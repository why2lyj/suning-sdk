# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class DiscountApplyAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyHead = None
        self.applyDetail = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'applyDiscountApplication'

    def getApiMethod(self):

        return 'suning.application.discount.apply'



