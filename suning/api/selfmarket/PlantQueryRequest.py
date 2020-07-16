# -*- coding: utf-8 -*-

'''

Created on 2018-10-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class PlantQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.beginDate = None
        self.endDate = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'beginDate':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryPlant'

    def getApiMethod(self):

        return 'suning.selfmarket.plant.query'



