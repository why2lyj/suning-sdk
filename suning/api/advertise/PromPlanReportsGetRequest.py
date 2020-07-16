# -*- coding: utf-8 -*-

'''

Created on 2016-11-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromPlanReportsGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionId = None
        
        self.setParamRule({
        	'promotionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getPromPlanReports'

    def getApiMethod(self):

        return 'suning.advertise.promplanreports.get'



