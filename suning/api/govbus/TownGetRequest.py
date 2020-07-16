# -*- coding: utf-8 -*-

'''

Created on 2020-6-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class TownGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.transportCode = None
        
        self.setParamRule({
        	'transportCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getTown'

    def getApiMethod(self):

        return 'suning.govbus.town.get'



