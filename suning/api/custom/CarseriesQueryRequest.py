# -*- coding: utf-8 -*-

'''

Created on 2019-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class CarseriesQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.brandId = None
        
        self.setParamRule({
        	'brandId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCarseries'

    def getApiMethod(self):

        return 'suning.custom.carseries.query'



