# -*- coding: utf-8 -*-

'''

Created on 2018-4-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExpensesrebateapplyQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applicationCode = None
        self.applyBegindate = None
        self.applyEnddate = None
        self.applyModel = None
        self.checkedBegindate = None
        self.checkedEnddate = None
        self.pageNo = None
        self.pageSize = None
        self.snCode = None
        self.supplierCode = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryExpensesRebateapply'

    def getApiMethod(self):

        return 'suning.selfmarket.expensesrebateapply.query'



