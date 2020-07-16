# -*- coding: utf-8 -*-

'''

Created on 2018-9-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class BjcpcunitdetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.companyCode = None
        self.countDate = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'companyCode':{'allow_empty':False},
        	'countDate':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryBjcpcunitdetail'

    def getApiMethod(self):

        return 'suning.advertise.bjcpcunitdetail.query'



