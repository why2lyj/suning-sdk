# -*- coding: utf-8 -*-

'''

Created on 2015-11-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class LogisticsDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.expressCompanyCode = None
        self.expressNo = None
        
        self.setParamRule({
        	'expressCompanyCode':{'allow_empty':False},
        	'expressNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getLogisticsDetail'

    def getApiMethod(self):

        return 'suning.fourps.logisticsdetail.get'



