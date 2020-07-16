# -*- coding: utf-8 -*-

'''

Created on 2020-4-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class CrowdcountbystrategyQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.strategy = None
        
        self.setParamRule({
        	'strategy':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCrowdcountbystrategy'

    def getApiMethod(self):

        return 'suning.custom.crowdcountbystrategy.query'



