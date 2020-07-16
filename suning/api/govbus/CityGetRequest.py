# -*- coding: utf-8 -*-

'''

Created on 2020-6-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class CityGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.transportCode = None
        
        self.setParamRule({
        	'transportCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCity'

    def getApiMethod(self):

        return 'suning.govbus.city.get'



