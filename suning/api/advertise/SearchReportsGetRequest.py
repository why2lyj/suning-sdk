# -*- coding: utf-8 -*-

'''

Created on 2016-11-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class SearchReportsGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionUnitId = None
        self.terminalType = None
        
        self.setParamRule({
        	'promotionUnitId':{'allow_empty':False},
        	'terminalType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getSearchReports'

    def getApiMethod(self):

        return 'suning.advertise.searchreports.get'



