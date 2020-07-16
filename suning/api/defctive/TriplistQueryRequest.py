# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class TriplistQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.tripEndTime = None
        
        self.setParamRule({
        	'tripEndTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryTriplist'

    def getApiMethod(self):

        return 'suning.defctive.triplist.query'



