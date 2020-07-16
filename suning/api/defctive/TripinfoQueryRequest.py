# -*- coding: utf-8 -*-

'''

Created on 2020-4-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class TripinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.tripCode = None
        
        self.setParamRule({
        	'tripCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryTripinfo'

    def getApiMethod(self):

        return 'suning.defctive.tripinfo.query'



