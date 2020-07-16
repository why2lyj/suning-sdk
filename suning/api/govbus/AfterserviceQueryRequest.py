# -*- coding: utf-8 -*-

'''

Created on 2019-6-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class AfterserviceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityId = None
        self.countyId = None
        self.orderId = None
        self.skus = None
        
        self.setParamRule({
        	'cityId':{'allow_empty':False},
        	'countyId':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryAfterservice'

    def getApiMethod(self):

        return 'suning.govbus.afterservice.query'



