# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PlantInfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.plantTypeCode = None
        self.cityName = None
        self.plantCode = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'plantTypeCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryPlantInfo'

    def getApiMethod(self):

        return 'suning.plantinfo.query'



