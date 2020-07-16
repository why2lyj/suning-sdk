# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class StatementCodeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.createTimeStart = None
        self.createTimeEnd = None
        self.supplierCode = None
        self.operaType = None
        self.isSing = None
        self.isSuccess = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'createTimeStart':{'allow_empty':False},
        	'createTimeEnd':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryStatementCode'

    def getApiMethod(self):

        return 'suning.statementcode.query'



