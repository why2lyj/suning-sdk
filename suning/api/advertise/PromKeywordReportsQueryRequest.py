# -*- coding: utf-8 -*-

'''

Created on 2016-11-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromKeywordReportsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionStartDate = None
        self.promotionEndDate = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'promotionStartDate':{'allow_empty':False},
        	'promotionEndDate':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryPromKeywordReports'

    def getApiMethod(self):

        return 'suning.advertise.promkeywordreports.query'



