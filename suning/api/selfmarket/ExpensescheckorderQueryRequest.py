# -*- coding: utf-8 -*-

'''

Created on 2018-3-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExpensescheckorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applicationCode = None
        self.applyCode = None
        self.createBegindate = None
        self.createEnddate = None
        self.modelType = None
        self.pageNo = None
        self.pageSize = None
        self.status = None
        self.supplierCode = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryExpensescheckorder'

    def getApiMethod(self):

        return 'suning.selfmarket.expensescheckorder.query'



