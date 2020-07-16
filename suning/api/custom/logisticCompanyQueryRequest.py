# -*- coding: utf-8 -*-

'''

Created on 2020-5-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class logisticCompanyQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'logisticCompany'

    def getApiMethod(self):

        return 'suning.custom.logisticcompany.query'



