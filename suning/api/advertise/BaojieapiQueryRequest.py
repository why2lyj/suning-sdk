# -*- coding: utf-8 -*-

'''

Created on 2018-5-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class BaojieapiQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.countDate = None
        self.companyCode = None
        
        self.setParamRule({
        	'countDate':{'allow_empty':False},
        	'companyCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryBaojieapi'

    def getApiMethod(self):

        return 'suning.advertise.baojieapi.query'



