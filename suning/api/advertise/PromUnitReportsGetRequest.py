# -*- coding: utf-8 -*-

'''

Created on 2016-11-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromUnitReportsGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionUnitId = None
        
        self.setParamRule({
        	'promotionUnitId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getPromUnitReports'

    def getApiMethod(self):

        return 'suning.advertise.promunitreports.get'



