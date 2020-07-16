# -*- coding: utf-8 -*-

'''

Created on 2020-3-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class IssueinvoicesrcdomsCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.invoiceIssueReqDTO = None
        self.respList = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'createIssueinvoicesrcdoms'

    def getApiMethod(self):

        return 'suning.retailer.issueinvoicesrcdoms.create'



