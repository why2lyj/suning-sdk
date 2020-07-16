# -*- coding: utf-8 -*-

'''

Created on 2018-5-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class BjcptQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.companyCode = None
        self.queryDate = None
        
        self.setParamRule({
        	'companyCode':{'allow_empty':False},
        	'queryDate':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryBjcpt'

    def getApiMethod(self):

        return 'suning.advertise.bjcpt.query'



