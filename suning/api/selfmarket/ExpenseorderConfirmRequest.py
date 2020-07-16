# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExpenseorderConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.detail = None
        self.head = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmExpenseorder'

    def getApiMethod(self):

        return 'suning.selfmarket.expenseorder.confirm'



